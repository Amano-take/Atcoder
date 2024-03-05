import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8
2 0 2 4 0 2 0 3
5
1 8 3
10 12 11
3 3 2
3 6 5
12 0 11
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
hq = []
heapq.heapify(hq)
N = int(input())
As = [int(input()) for _ in range(N)]
As.sort()
heapq.heappush(hq, (As[0]*As[0], 0, 0))
ans = 0
ex = set()

while len(hq) != 0:
    a, i, j = heapq.heappop(hq)
    if a > As[-1]:
        print(ans)
        exit()
    
    if bisect.bisect_right(As, a) - bisect.bisect_left(As, a) > 0:
        if i != j:
            ans += 2 * (bisect.bisect_right(As, a) - bisect.bisect_left(As, a))
        else:
            ans += bisect.bisect_right(As, a) - bisect.bisect_left(As, a)
    if j+1 < N and (i, j+1) not in ex:
        heapq.heappush(hq, (As[i]*As[j+1], i, j+1))
        ex.add((i, j+1))
    if i+1 <= j and (i+1, j) not in ex:
        heapq.heappush(hq, (As[i+1]*As[j], i+1, j))
        ex.add((i+1, j))
print(ans)