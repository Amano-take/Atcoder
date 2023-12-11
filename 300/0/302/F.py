import sys
import io
import math
from collections import defaultdict as ddict
import heapq
sys.setrecursionlimit(10**8)
_INPUT = """\
3 5
2
1 2
2
2 3
3
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N, M = map(int, input().split())
Graph = ddict(list)
for _ in range(N):
    _ = int(input())
    Ss = list(map(int, input().split()))
    Ss.sort()
    for s in Ss[1:]:
        Graph[Ss[0]].append(s)
        Graph[s].append(Ss[0])
    
hq = [(0, 1)]

#dijkstra
dist = [[float('inf'), -1] for _ in range(M+1)] 
dist[1] = [0, -1]
flag = False
while hq:
    d, v = heapq.heappop(hq)
    if v == M:
        print(d - 1)
        flag = True
        break
    if dist[v][0] < d:
        continue
    for nv in Graph[v]:
        if nv > v:
            cost = 1
        else:
            cost = 0

        if dist[nv][0] > dist[v][0] + cost:
            dist[nv][0] = dist[v][0] + cost
            dist[nv][1] = v
            heapq.heappush(hq, (dist[nv][0], nv))
if not flag:
    print(-1)
else:
    ans = []
    v = M
    while v != -1:
        ans.append(v)
        print(v, dist[v])
        v = dist[v][1]
    print(*ans[::-1])