import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
100 200 2
50 10 1
100 200 5
150 1 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
weight = ddict(lambda: inf)
graph = ddict(list)
for i in range(N-1):
    a, b, c = map(int, input().split())
    c -= 1
    graph[i].append(i+1)
    graph[i].append(c)
    weight[(i, i+1)] = a
    weight[(i, c)] = min(weight[(i, c)], b)

# dijkstra
start = 0
dist = [inf] * N
dist[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    d, v = heapq.heappop(q)
    if dist[v] < d:
        continue
    for u in graph[v]:
        if dist[u] > dist[v] + weight[(v, u)]:
            dist[u] = dist[v] + weight[(v, u)]
            heapq.heappush(q, (dist[u], u))

print(dist[N-1])
    