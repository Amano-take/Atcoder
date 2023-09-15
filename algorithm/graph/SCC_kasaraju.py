import sys
import io
from collections import defaultdict as ddict
from collections import deque
sys.setrecursionlimit(10**8)

_INPUT="""\
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3
"""
sys.stdin=io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, readline().split())
edge = ddict(set)
reverseedge = ddict(set)
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, readline().split())
    edge[A].add(B)
    reverseedge[B].add(A)

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
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
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
_, G = construct(N, edge, label, group)
ans = 0
for g in G:
    ans += len(g) * (len(g) - 1) / 2
print(int(ans))

        