import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 3
4 3
9 5
15 8
8 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
hq = []
for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(hq, -b)
    heapq.heappush(hq, -a+b)
ans = 0
for i in range(K):
    ans -= heapq.heappop(hq)
print(ans)