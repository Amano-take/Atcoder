import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10 4
0 3
3 5
2 7
9 0
5 6
4 3
7 8
6 5
9 9
2 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[inf] * (K + 1) for _ in range(1 << N)]
for g in range(K+1):
    dp[0][g] = 0


bitcount = [[] for _ in range(N+1)]
for i in range(1 << N):
    bc = bin(i).count("1")
    bitcount[bc].append(i)

for bc, ss in enumerate(bitcount):
    if bc <= 1:
        for s in ss:
            dp[s][1] = 0
    elif bc == 2:
        for s in ss:
            i, j = [k for k in range(N) if s >> k & 1]
            dp[s][1] = (XY[i][0] - XY[j][0])**2 + (XY[i][1] - XY[j][1])**2
    else:
        for s in ss:
            t = [k  for k in range(N) if s >> k & 1][0]
            temp = 0
            for i in range(N):
                if s >> i & 1 and i != t:
                    temp = max(temp, (XY[i][0] - XY[t][0])**2 + (XY[i][1] - XY[t][1])**2)
            dp[s][1] = max(dp[s - (1 << t)][1], temp)

for g in range(2, K+1):
    for s in range(0, 1 << N):
        if bin(s).count("1") <= g:
            dp[s][g] = 0
            continue
        temp = inf
        sub = s
        while sub:
            sub = (sub - 1) & s
            temp = min(temp, max(dp[s-sub][g-1], dp[sub][1]))
        dp[s][g] = temp

print(dp[(1 << N) - 1][K])