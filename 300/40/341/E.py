import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

from typing import TypeVar, Callable, Sequence
 
TypeS = TypeVar('TypeS')
TypeT = TypeVar('TypeT')
 
 
class LazySegmentTreeInjectable:
    def __init__(
            self,
            n: int,
            operation: Callable[[TypeS, TypeS], TypeS],
            mapping: Callable[[TypeS, TypeT, int], TypeS],
            composition: Callable[[TypeT, TypeT], TypeT],
            e_factory: Callable[[], TypeS],
            id_factory: Callable[[], TypeT], ):
        n2 = 1 << (n - 1).bit_length()
        self.offset = n2
        self.operation = operation
        self.mapping = mapping
        self.composition = composition
        self.e_factory = e_factory
        self.id_factory = id_factory
        self.data = [e_factory() for _ in range(n2 << 1)]
        self.lazy = [id_factory() for _ in range(n2 << 1)]
 
    @classmethod
    def from_array(
            cls,
            arr: Sequence[TypeS],
            operation: Callable[[TypeS, TypeS], TypeS],
            mapping: Callable[[TypeS, TypeT, int], TypeS],
            composition: Callable[[TypeT, TypeT], TypeT],
            e_factory: Callable[[], TypeS],
            id_factory: Callable[[], TypeT], ):
        ins = cls(len(arr), operation, mapping, composition, e_factory, id_factory)
        data = ins.data
        op = ins.operation
        data[ins.offset:ins.offset + len(arr)] = arr
        for i in range(ins.offset - 1, 0, -1):
            l = i << 1
            data[i] = op(data[l], data[l + 1])
        return ins
 
    def _propagate(self, i):
        data = self.data
        lazy = self.lazy
 
        if i < self.offset:
            l = i << 1
            r = l + 1
            lazy[l] = self.composition(lazy[l], lazy[i])
            lazy[r] = self.composition(lazy[r], lazy[i])
 
        k = self.offset >> (i.bit_length() - 1)
        data[i] = self.mapping(data[i], lazy[i], k)
        lazy[i] = self.id_factory()
 
    def _recalculate(self, i):
        if i >= self.offset:
            return
        l = i << 1
        r = l + 1
        k = self.offset >> i.bit_length()
        l_dat = self.mapping(self.data[l], self.lazy[l], k)
        r_dat = self.mapping(self.data[r], self.lazy[r], k)
        self.data[i] = self.operation(l_dat, r_dat)
 
    def _get_overhead_indices(self, l, r):
        """ l, r are already added offset """
        result = []
        #kisuu ni naru made agatteiku kisuu no sono ikkoue wo sasu
        l0 = (l // (l & -l)) >> 1
        r0 = (r // (r & -r)) >> 1
        while l0 != r0:
            if l0 > r0:
                result.append(l0)
                l0 >>= 1
            else:
                result.append(r0)
                r0 >>= 1
        while l0:
            result.append(l0)
            l0 >>= 1
        return result
 
    def apply(self, l: int, r: int, x: TypeT):
        lazy = self.lazy
        cp = self.composition
        l = max(0, l)
        r = min(self.offset + 1, r)
        l += self.offset
        r += self.offset
        #kodomo ga kawaru node no list (sita kara ue)
        rc_indices = self._get_overhead_indices(l, r)
 
        #kokohanakutemo ikeru (kakann)
        #seiyaku toshite ue ni huruinowo yurusanai -> ueni kakono ga aru baai ha oroshite kuru
        #"""
        for i in reversed(rc_indices):
            self._propagate(i)
        #"""
        while l < r:
            if l & 1:
                lazy[l] = cp(lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                lazy[r] = cp(lazy[r], x)
            l >>= 1
            r >>= 1
 
        for i in rc_indices:
            self._recalculate(i)
 
    def query(self, l: int, r: int) -> TypeS:
        data = self.data
        lazy = self.lazy
        op = self.operation
        mp = self.mapping
 
        l += self.offset
        r += self.offset
        rc_indices = self._get_overhead_indices(l, r)
 
        for i in reversed(rc_indices):
            self._propagate(i)
 
        res_l = self.e_factory()
        res_r = self.e_factory()
        k = 1
        #rikai (1~15, [9, 14)) de ez
        while l < r:
            if l & 1:
                res_l = op(res_l, mp(data[l], lazy[l], k))
                l += 1
            if r & 1:
                r -= 1
                res_r = op(mp(data[r], lazy[r], k), res_r)
            l >>= 1
            r >>= 1
            k <<= 1
 
        return op(res_l, res_r)
 
    def debug_print(self):
        i = 1
        while i <= self.offset:
            print(self.data[i:2 * i])
            i <<= 1
        print('--------')
        i = 1
        while i <= self.offset:
            print(self.lazy[i:2 * i])
            i <<= 1
        print()
_INPUT = """\
5 6
10100
2 1 3
2 1 5
1 1 4
2 1 5
1 3 3
2 2 4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, Q = map(int, input().split())
S = input()
def op(x, y):
    is_goodx, leftx, rightx = unpack(x)
    is_goody, lefty, righty = unpack(y)
    if leftx == None:
        return y
    if righty == None:
        return x
    
    if rightx != lefty:
        return pack(is_goodx and is_goody, leftx, righty)
    else:
        return pack(False, leftx, righty)
    
def mapping(x, f, k):
    is_good, left, right = unpack(x)
    if f:
        return pack(is_good, 1-left, 1-right)
    else:
        return x
    
def composition(f, g):
    return f ^ g

def e_factory():
    return pack(True, None, None)

def id_factory():
    return False

def pack(is_good, left, right):
    ans = 0
    ans += is_good << 4
    if left is None:
        ans += 1 << 2
    else:
        ans += left << 3
    if right is None:
        ans += 1
    else:
        ans += right << 1
    return ans

def unpack(x):
    is_good = (x >> 4) & 1
    if (x >> 2) & 1:
        left = None
    else:
        left = (x >> 3) & 1
    if x & 1:
        right = None
    else:
        right = (x >> 1) & 1
    return (is_good, left, right)

lst = LazySegmentTreeInjectable.from_array([pack(True, 0, 0) if c == "0" else pack(True, 1, 1) for c in S], op, mapping, composition, e_factory, id_factory)

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        lst.apply(a-1, b, True)
    else:
        if unpack(lst.query(a-1, b))[0]:
            print("Yes")
        else:
            print("No")
