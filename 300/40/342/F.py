import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
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
sys.setrecursionlimit(10**8)
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, L, D = map(int, input().split())

def op(a, b):
    return a + b

def mp(a, b, k):
    return a + b

def cp(a, b):
    return a + b

def e_factory():
    return 0

def id_factory():
    return 0

lst = LazySegmentTreeInjectable.from_array([0] * (L + D), op, mp, cp, e_factory, id_factory)
lst.apply(0, 1, 1)

for i in range(0, L):

    pi = lst.query(i, i+1)
    lst.apply(i+1, i+1+D, pi/D)
    lst.apply(i, i+1, -pi)


ruiseki = [0]
for i in range(L + D):
    ruiseki.append(ruiseki[-1] + lst.query(i, i+1))


#ここが違う
left = 0
right = N
while left != right -1:
    mid = (left + right) // 2
    wr = 0
    for i in range(mid+1, min(mid + D + 1, N+1)):
        wr += ruiseki[i] / D
    if ruiseki[mid]  <  wr:
        left = mid
    else:
        right = mid

lstp = LazySegmentTreeInjectable.from_array([0] * (N + D), op, mp, cp, e_factory, id_factory)
lstp.apply(0, 1, 1)
for i in range(0, left+1):
    pi = lstp.query(i, i+1)
    lstp.apply(i+1, min(i+1+D, N-1+D), pi/D)
    lstp.apply(i, i+1, -pi)


ans = 0
for i in range(left+1, left + D+1):
    ans += ruiseki[i] * lstp.query(i, i+1)
ans += ruiseki[-1] - ruiseki[N+1]
print(ans)