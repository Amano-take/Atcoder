import sys
import io
import math
import heapq
sys.setrecursionlimit(10**8)
inf = float("inf")
_INPUT = """\
4 8 5 13
0 6 2 15
6 0 3 5
2 3 0 13
15 5 13 0
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, A, B, C = map(int, readline().split())
graphA = [0] * (N**2)
graphB = [0]* (N**2)
for i in range(N):
    for j, d in enumerate(map(int, readline().split())):
        graphA[i*N + j] = d * A
        graphB[i*N + j] = d * B + C

def dijkstra(start, graph, graphsize):
    ans = [inf] * graphsize
    heap = [(0, start)]
    seen = set()
    while len(seen) != graphsize:
        c, p = heapq.heappop(heap)
        if p not in seen:
            ans[p] = c
            seen.add(p)
        else:
            continue
        for next in range(graphsize):
            if next not in seen:
                cost = graph[p*graphsize + next]
                heapq.heappush(heap, (cost+c, next))
    return ans

syayou = dijkstra(0, graphA, N)
dehsya = dijkstra(N-1, graphB, N)
ans = inf
for i in range(N):
    ans = min(ans, syayou[i]+dehsya[i])
print(ans)

