import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

sys.setrecursionlimit(10**8)
_INPUT = """\
100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
W, N = map(int, input().split())
lrv = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (W + 1) for _ in range(N+1)]
dp[0][0] = 0

def op(x, y):
    return max(x, y)

def e():
    return -1

seg = SegTree(op, e, W+1, dp[0])

for i in range(N):
    l, r, v = lrv[i]

    for w in range(W, -1, -1):
        dp[i+1][w] = dp[i][w]
        #choose
        left = max(w - r, 0)
        right = max(w - l + 1, 0)
        if left == right:
            continue

        next = seg.prod(left, right) + v
        if next == v - 1:
            continue
        
        if dp[i][w] < next:
            dp[i+1][w] = next
            seg.set(w, next)


print(dp[N][W])

