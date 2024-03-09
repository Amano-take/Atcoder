import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

K = int(input())
if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 1)
dp[0] = 1
for i in range(1, K + 1):
    for j in range(1, min(10, i + 1)):
        dp[i] += dp[i - j]
        dp[i] %= 10**9 + 7
print(dp[K])