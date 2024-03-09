import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
1 3
2 4
3 5
2 5
3 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
Graph = ddict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

queue = deque([(1, 1)])
color = [-1] * (N+1)
color[1] = 1

while queue:
    vc = queue.popleft()
    v, c = vc
    for u in Graph[v]:
        if color[u] == -1:
            color[u] = 1 - c
            queue.append((u, 1-c))

blacks = []
whites = []
for i in range(1, N+1):
    if color[i] == 1:
        blacks.append(i)
    if color[i] == 0:
        whites.append(i)

if len(blacks) >= len(whites):
    print(*blacks[0:N //2])
else:
    print(*whites[0:N//2])