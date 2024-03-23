import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 3
3
1 2 3
2
3 4
2
5 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
graph = ddict(list)
for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    super_node = -i - 1
    for aa in a:
        graph[aa].append(super_node)
        graph[super_node].append(aa)

def bfs(start):
    q = deque([start])
    dist = ddict(lambda: inf)
    dist[start] = 0
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == inf:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist

dist = bfs(1)
for i in range(1, N+1):
    if i in dist:
        print(dist[i] // 2)
    else:
        print(-1)