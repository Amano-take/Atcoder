import sys
import io
import heapq
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
1 8
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N, M = map(int, readline().split())
ans = [0] * N
event = []
queue = [i for i in range(N)]

for _ in range(M):
    t, w, s = map(int, readline().split())
    while len(event) != 0:
        et, p = heapq.heappop(event)
        if et <= t:
            heapq.heappush(queue, p)
        else:
            heapq.heappush(event, (et, p))
            break
    if len(queue) != 0:
        p = heapq.heappop(queue)
        ans[p] += w
        heapq.heappush(event, (t+s, p))

for a in ans:
    print(a)