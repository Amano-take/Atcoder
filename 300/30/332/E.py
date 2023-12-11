import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 3
3 5 3 6 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, D = map(int, input().split())
Ws = list(map(int, input().split()))
ave = sum(Ws) / D
dp = [[inf] * (1 << N) for _ in range(D+1)]
subset = [[0]  for _ in range(1 << N)]
for i in range(1 << N):
    sub = i
    while True:
        subset[i].append(sub)
        sub = (sub - 1) & i
        if sub == 0:
            break


for i in range(1 << N):
    weight = 0
    for j in range(N):
        if i & (1 << j):
            weight += Ws[j]
    dp[1][i] = (weight - ave) ** 2

for k in range(2, D+1):
    for set in range(1 << N):
        subset = set
        while subset != 0:
            dp[k][set] = min(dp[k][set], dp[k-1][set - subset] + dp[1][subset])
            subset = (subset - 1) & set
        else:
            dp[k][set] = min(dp[k][set], dp[k-1][set] + dp[1][0])
print(dp[D][(1 << N) - 1] / D)