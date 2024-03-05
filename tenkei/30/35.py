import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product

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

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
1 2
2 3
3 4
1 5
3 6
5
3 1 2 3
3 1 2 5
3 1 3 6
3 3 4 5
3 4 5 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
graph = ddict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

euler_tour = []
depth = []
first_appear = [-1] * (N+1)
def dfs(v, d):
    first_appear[v] = len(euler_tour)
    euler_tour.append(v)
    depth.append(d)
    for u in graph[v]:
        if first_appear[u] != -1:
            continue
        dfs(u, d+1)
        euler_tour.append(v)
        depth.append(d)
dfs(1, 0)


# LCA
vs = list(zip(depth, euler_tour))
def op(x, y):
    dx, vx = x
    dy, vy = y
    if dx < dy:
        return x
    else:
        return y
depth_v = [-1]
for i in range(len(first_appear)-1):
    depth_v.append(depth[first_appear[i+1]])
st = SegTree(op, lambda: (inf, inf), len(vs), vs)
def lca(u, v):
    l = first_appear[u]
    r = first_appear[v]
    if l > r:
        l, r = r, l
    return st.prod(l, r+1)[1]

def dist(u, v):
    lca_uv = lca(u, v)
    return depth_v[u] + depth_v[v] - 2 * depth_v[lca_uv]

Q = int(input())
for _ in range(Q):
    k, *v = map(int, input().split())
    ans = 0
    at = [(first_appear[v[i]], v[i]) for i in range(k)]
    at.sort()
    for i in range(k-1):
        ans += dist(at[i][1], at[i+1][1])
    ans += dist(at[k-1][1], at[0][1])
    print(ans//2)
    