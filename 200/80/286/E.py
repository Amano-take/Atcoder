import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
30 50 70 20 60
NYYNN
NNYNN
NNNYY
YNNNN
YNNNN
3
1 3
3 1
4 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
graph = ddict(list)
for j in range(N):
    s = input()
    for i in range(N):
        if s[i] == "Y":
            graph[j].append(i)

ansr = []
ansd = []
for i in range(N):
    #start = i, dijkstra
    dist = [inf] * N
    reward = [0] * N
    dist[i] = 0
    reward[i] = -As[i]
    que = [(0, -As[i], i)]
    heapq.heapify(que)
    while que:
        d, r, v = heapq.heappop(que)
        for nv in graph[v]:
            if dist[nv] > d + 1:
                dist[nv] = d + 1
                reward[nv] = r - As[nv]
                heapq.heappush(que, (d + 1, r - As[nv], nv))
    ansr.append(reward)
    ansd.append(dist)
for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if ansd[a][b] == inf:
        print("Impossible")
    else:
        print(ansd[a][b], -ansr[a][b])