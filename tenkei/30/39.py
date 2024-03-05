import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
12
1 2
3 1
4 2
2 5
3 6
3 7
8 4
4 9
10 5
11 7
7 12
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
graph = ddict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

chnum = [0] * (N+1)
def dfs(v, p):
    res = 1
    for u in graph[v]:
        if u == p:
            continue
        res += dfs(u, v)
    chnum[v] = res
    return res

dfs(1, -1)

ans = 0
for i in range(2, N+1):
    ans += chnum[i] * (N-chnum[i])
print(ans)