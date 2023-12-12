import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 7
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
if N * N < M:
    print("-1")
    exit()

ans = inf
for i in range(1, math.ceil(math.sqrt(M)) + 1):
    if math.ceil(M / i) > N:
        continue
    else:
        ans = min(ans, i * math.ceil(M / i))
print(ans)