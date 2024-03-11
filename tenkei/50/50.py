import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, L = map(int, input().split())
MOD = 10 ** 9 + 7
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-L]
    dp[i] %= MOD
print(dp[N])