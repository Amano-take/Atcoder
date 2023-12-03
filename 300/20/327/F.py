import heapq
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
from collections import defaultdict, deque



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
 
        l += self.offset
        r += self.offset

        rc_indices = self._get_overhead_indices(l, r)
        """
        for i in reversed(rc_indices):
            self._propagate(i)
        """

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
8 4 3
1 1
3 4
6 4
5 2
4 2
4 3
5 5
7 3
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, D, W = map(int, readline().split())
schedule = [defaultdict(int) for _ in range(2 * 10 ** 5 + 1)]
maxX = 0
for i in range(N):
    t, x = map(int, readline().split())
    if maxX < x:
        maxX = x
    schedule[t][x] += 1
    if t + D < len(schedule):
        schedule[t+D][x] -= 1

def funcvv(a, b):
    return max(a, b)
def funcva(v, a, c):
    return v + a
def funcaa(a1, a2):
    return a1 + a2
def funce():
    return 0
def funcid():
    return 0

lst = LazySegmentTreeInjectable(maxX, funcvv, funcva, funcaa, funce, funcid)
ans = 0
for Xs in schedule:
    for k, v in Xs.items():
        if v != 0:
            lst.apply(max(0, k-W), k, v)
    ans = max(ans, lst.query(0, maxX))
print(ans)