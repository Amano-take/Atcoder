import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10000000 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())

# eratosthenes'

thieve = [0] * (N + 1)
thieve[0] = 0
ans = 0
for i in range(2, N+1):
    if thieve[i] == 0:
        for j in range(i, N+1, i):
            thieve[j] += 1
    if thieve[i] >= K:
        ans += 1
print(ans)