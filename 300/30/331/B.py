import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
16 120 150 200
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, S, M, L = map(int, input().split())
dp = [inf] * (N+24)
dp[0] = 0
for i in range(N+11):
    dp[i+6] = min(dp[i+6], dp[i] + S)
    dp[i+8] = min(dp[i+8], dp[i] + M)
    dp[i+12] = min(dp[i+12], dp[i] + L)
print(min(dp[N:]))