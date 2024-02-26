import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
from sortedcontainers import SortedList
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
2 7 1 8 2 8
15
3 1
3 3
3 4
1 1 5 4
3 1
3 3
3 4
1 3 6 9
3 1
3 3
3 4
2 4
3 1
3 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()


N = int(input())
As = list(map(int, input().split()))

def composition(f, x):
    heapq.heappush(f, x)
    return f


def id_factory():
    x = []
    heapq.heapify(x)
    return x

class FunLazySegTree:
    def __init__(self, N, comp, id_factory):
        self.N = N
        self.comp = comp
        self.id_factory = id_factory
        self.offset = 1 << (N - 1).bit_length()
        self.lazy = [id_factory() for _ in range(self.offset << 1)]
        self.delete = [id_factory() for _ in range(self.offset << 1)]

    
    def apply(self, l, r, x):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.lazy[l] = self.comp(self.lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.comp(self.lazy[r], x)
            l >>= 1
            r >>= 1
    
    def get(self, x):
        lazy = self.lazy[x]
        delete = self.delete[x]
        while len(delete) > 0 and delete[0] == lazy[0]:
            heapq.heappop(lazy)
            heapq.heappop(delete)
        if len(lazy) == 0:
            return -1    
        return lazy[0]
    
    def query(self, x):
        x += self.offset
        res = 0
        while x > 0:
            res = min(res, self.get(x))
            x >>= 1
        return res
    
    def debug_print(self):
        i = 1
        while i <= self.offset:
            print(self.lazy[i:2 * i])
            i <<= 1
        print()

        i = 1 
        while i <= self.offset:
            print(self.delete[i:2 * i])
            i <<= 1
        print()
    

    def delete_apply(self, l, r, x):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.delete[l] = self.comp(self.delete[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.delete[r] = self.comp(self.delete[r], x)
            l >>= 1
            r >>= 1

seg = FunLazySegTree(N, composition, id_factory)
Q = int(input())
delete = ddict(list)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        seg.apply(q[1] - 1, q[2], -q[3])
        delete[i+1] = [q[1] - 1, q[2], -q[3]]
    elif q[0] == 2:
        seg.delete_apply(*delete[q[1]])
    else:
        x = seg.query(q[1] - 1)

        print(max(-x, As[q[1] - 1]))
           

