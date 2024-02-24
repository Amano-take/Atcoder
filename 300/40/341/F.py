import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 6
1 2
2 3
3 1
3 4
1 5
5 6
9 2 3 1 4 4
1 0 0 0 0 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph.append((a, b))

Ws = list(map(int, input().split()))
As = list(map(int, input().split()))

graphd = ddict(list)
for a, b in graph:
    if Ws[a] > Ws[b]:
        graphd[a].append(b)
    elif Ws[a] < Ws[b]:
        graphd[b].append(a)

def backpack_problem(W, ws, vs):
    dp = [0] * (W + 1)
    for i in range(len(ws)):
        for w in range(W, ws[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - ws[i]] + vs[i])
    return dp[W-1]

values = [-1] * N

def dfs(v):
    if values[v] != -1:
        return
    
    if len(graphd[v]) == 0:
        values[v] = 1
        return
    vs = []
    ws = []
    for next in graphd[v]:
        dfs(next)
        vs.append(values[next])
        ws.append(Ws[next])
    values[v] = backpack_problem(Ws[v], ws, vs) + 1

for i in range(N):
    dfs(i)

ans = 0
for i in range(N):
    ans += As[i] * values[i]

print(ans)
