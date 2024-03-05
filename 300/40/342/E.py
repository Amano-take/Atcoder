import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 7
10 5 10 3 1 3
13 5 10 2 3 4
15 5 10 7 4 6
3 10 2 4 2 5
7 10 2 3 5 6
5 3 18 2 2 3
6 3 20 4 2 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
Graph = ddict(list)
max_t = -1
max_s = -1
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    Graph[B].append((l, d, k, c, A))
    if B == N and l + (k-1) * d + c > max_t:
        max_t = l + (k-1) * d + c

# dijkstra
heap = []
answer = [-1] * (N+1)
heapq.heappush(heap, (-max_t, N))
answer[N] = max_t
while heap:
    t, v = heapq.heappop(heap)
    t = -t
    if t < answer[v]:
        continue
    for l, d, k, c, u in Graph[v]:
        start = t - c
        if  start < l:
            continue
        else:
            n = (start - l) // d + 1
            start = min(l + (n-1) * d, l + (k-1) * d)
            if start > answer[u]:
                answer[u] = start
                heapq.heappush(heap, (-start, u))
for i in range(1, N):
    if answer[i] == -1:
        print("Unreachable")
    else:
        print(answer[i])



