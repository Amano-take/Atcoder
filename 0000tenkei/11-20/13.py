import math
import sys
import io
import bisect
from collections import defaultdict, deque
from heapq import heappop, heappush
sys.setrecursionlimit(10**8)

_INPUT = """\
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
ans = [-1] * N
path = defaultdict(defaultdict)
readlines = sys.stdin.readlines()
for l in readlines:
    a, b, c = map(lambda x: int(x) - 1, l.split())
    path[a][b] = c + 1
    path[b][a] = c + 1


def dijkstra(path, start):
    dis = []
    heappush(dis, (0, start))
    ans = [-1]*len(path)
    searched = set()
    while len(dis) != 0:
        v, p = heappop(dis)
        if p in searched:
            continue
        searched.add(p)
        ans[p] = v
        for next in path[p]:
            cost = path[p][next]
            if next in searched:
                continue
            heappush(dis, (cost+v, next))
    return ans
go = dijkstra(path, 0)
ret = dijkstra(path, N-1)

for i in range(N):
    print(go[i] + ret[i])


