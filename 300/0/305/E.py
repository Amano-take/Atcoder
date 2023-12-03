import sys
import io
import math
from collections import defaultdict as ddict, deque
import heapq
sys.setrecursionlimit(10**8)
_INPUT = """\
10 10 2
2 1
5 1
6 1
2 4
2 5
2 10
8 5
8 6
9 6
7 9
3 4
8 2
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N, M, K = map(int, readline().split())
graph = ddict(list)
for _ in range(M):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

health = [ -1] * (N + 1)
hq = []
for _ in range(K):
    p, h = map(int, readline().split())
    heapq.heappush(hq, (-h, p))
    health[p] = max(health[p], h)

while len(hq) > 0:
    h, p = heapq.heappop(hq)
    h = -h
    for next in graph[p]:
        if health[next] < h-1:
            health[next] = h-1
            heapq.heappush(hq, (-h + 1, next))

ans = []
for i in range(1, N+1):
    if health[i] >= 0:
        ans.append(i)

print(len(ans))
print(*ans)
