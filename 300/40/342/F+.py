import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
from typing import TypeVar, Callable, Sequence
 
TypeS = TypeVar('TypeS')
TypeT = TypeVar('TypeT')
 
sys.setrecursionlimit(10**8)
_INPUT = """\
3 1 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, L, D = map(int, input().split())
p = [0] * (L + D + 1)
p[0] = 1
cur = 1 / D
for i in range(1,L + D + 1):
    if i > D:
        cur -= p[i - D - 1] / D
    p[i] = cur
    if i < L:
        cur += p[i] / D


imos = [0] * (L + D + 1) 
imos[0] = 1
imos[1] = -1
for i in range(0, L):
    p = imos[i]
    imos[i+1] += p / D
    imos[i+1+D] -= p / D
    imos[i+1] += p
for i in range(L, L + D):
    imos[i+1] += imos[i]

ysum = [0]
for i in range(L + D):
    if i < L:
        ysum.append(ysum[-1])
    else:
        ysum.append(ysum[-1] + imos[i])
while len(ysum) < N + D + 1:
    ysum.append(ysum[-1])


win_rate = [0] * (N + D)
for i in range(N + D):
    if i > N:
        win_rate[i] = 0
    else:
        win_rate[i] = ysum[min(i, N)] + ysum[-1] - ysum[N+1]

ans_dp = [0] * (N + D)

for i in range(N, N+D):
    ans_dp[i] = win_rate[i]


sum_x = sum([ans_dp[N-1+j] for j in range(1, D+1)])/D
for i in range(N-1, -1, -1):

    ans_dp[i] = max(win_rate[i], sum_x)
    sum_x -= ans_dp[i+D] / D
    sum_x += ans_dp[i] / D

print(ans_dp[0])
