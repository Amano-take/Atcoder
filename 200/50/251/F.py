import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 8
5 1
4 3
1 4
3 5
1 2
2 6
1 6
4 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
G = ddict(list)
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

spanning_tree = set()
ans = []
def dfs(v, t):
    if v in spanning_tree:
        return
    spanning_tree.add(v)
    if t != 0:
        ans.append((v, t))
    for u in G[v]:
        dfs(u, v)
dfs(1, 0)
for i in ans:
    print(*i)

spanning_tree = set()
ans = []
#bfs
q = deque([(1, 0)])
while q:
    v, t = q.popleft()
    if v in spanning_tree:
        continue
    spanning_tree.add(v)
    if t != 0:
        ans.append((v, t))
    for u in G[v]:
        q.append((u, v))
for i in ans:
    print(*i)
    