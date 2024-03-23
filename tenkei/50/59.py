import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

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

_INPUT = """\
6 6 3
1 3
2 4
1 4
4 6
5 6
1 5
2 6
1 5
3 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
edge = ddict(set)
reverseedge = ddict(set)

N, M, K = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].add(b)
    reverseedge[b].add(a)


def scc(N, edge, reverseedge):
    order = deque()
    scc = [None] * N
    used = [0] * N
    def dfs(s):
        used[s] = 1
        for t in edge[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        scc[s] = col
        used[s] = 1
        for t in reverseedge[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    while len(order) != 0:
        s = order.pop()
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, scc

def construct(N, edge, label, group):
    G0 = ddict(set)
    GP = ddict(list)
    for v in range(N):
        lbs = group[v]
        for w in edge[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

label, group = scc(N, edge, reverseedge)
G0, GP = construct(N, edge, label, group)
print(group)
#euler tour
et = []
et_first = [0] * label

def dfs(v, depth):
    et.append((v, depth))
    et_first[v] = len(et)
    for w in G0[v]:
        dfs(w, depth + 1)
        et.append((v, depth))

dfs(0, 0)
def op(x, y):
    vx, dx = x
    vy, dy = y
    if dx < dy:
        return x
    else:
        return y

st = SegTree(op, lambda: (0, inf), len(et), et)
for i in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if group[a] == group[b]:
        print("Yes")
    else:
        groupa = group[a]
        groupb = group[b]
        if groupb < groupa:
            groupa, groupb = groupb, groupa
            a, b = b, a
        lca = st.prod(et_first[group[a]], et_first[group[b]] + 1)
        if lca[0] == group[a]:
            print("Yes")
        else:
            print("No")



