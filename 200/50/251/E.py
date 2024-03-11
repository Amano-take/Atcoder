import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
2 5 3 2 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
dp = [inf] * (N+1)
dp[0] = 0
for i in range(N):
    if i >= 1:
        dp[i+1] = min(dp[i+1], dp[i] + A[i-1], dp[i-1] + A[i-1])
    else:
        dp[i+1] = A[i]

_dp = [inf] * (N+1)
_dp[0] = inf
_dp[1] = A[N-1]
for i in range(1, N):
    _dp[i+1] = min(_dp[i+1], _dp[i] + A[i-1], _dp[i-1] + A[i-1])

print(min(dp[N], _dp[N-1], _dp[N]))