import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 5
1 2
2 3
3 1
3 4
4 5
2
1 0
5 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
graph = ddict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

K = int(input())

mustwhite = [False] * (N+1)

def dijkstra(start, limit):
    #return points which is reachable from start in less than limit steps, and which is reachable just in limit steps
    ans2 = set()
    dist = [inf] * (N+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, u = heapq.heappop(q)
        if d == limit:
            ans2.add(u)
        elif d < limit:
            mustwhite[u] = True
        else:
            continue

        if d > dist[u]:
            continue
        for v in graph[u]:
            if dist[v] > d + 1:
                dist[v] = d + 1
                heapq.heappush(q, (dist[v], v))

    return ans2

orblack = []
for i in range(K):
    p, d = map(int, input().split())
    ans2 = dijkstra(p, d)
    orblack.append(ans2)

blackset = set()
for i in range(1, N+1):
    if mustwhite[i] == False:
        blackset.add(i)

for obset in orblack:
    if obset & blackset == set():
        print("No")
        exit()
else:
    print("Yes")
    ans = []
    for i in range(1, N+1):
        if mustwhite[i] == False:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))