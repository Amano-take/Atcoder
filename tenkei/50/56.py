import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 34
3 14
15 9
26 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, S = map(int, input().split())
dp = [["Impossible"] * (S+1) for _ in range(N+1)]
dp[0][0] = ""
for i in range(1, N+1):
    a, b = map(int, input().split())
    for j in range(S+1):
        change = set()
        if dp[i-1][j] != "Impossible":
            if j+a <= S and j+a not in change:
                change.add(j+a)
                dp[i][j+a] = dp[i-1][j] + "A"
            if j+b <= S and j+b not in change:
                change.add(j+b)
                dp[i][j+b] = dp[i-1][j] + "B"
print(dp[N][S])