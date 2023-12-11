import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 2 3 3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, A, B, P, Q = map(int, input().split())
DIV = 998244353
#dp[A][B] means how often takahashi is on pointA and aoki in on pointB.
#the answer is sum of dp[N][B] for all B except N.
dp = [[0] * (N - B +1) for _ in range(N - A + 1)]
PQDEVIDE = pow(P*Q, -1, DIV)
PDEVIDE = pow(P, -1, DIV)
dp[0][0] = 1
for demep in range(1, P+1):
    gta = min(A + demep, N) - A
    dp[gta][0] += dp[0][0] * PDEVIDE
for ta in range(A+1, N):
    for ao in range(B, N):
        for demep in range(1, P+1):
            for demeq in range(1, Q+1):
                gta = min(ta + demep, N) - A
                gao = min(ao + demeq, N) - B
                dp[gta][gao] += dp[ta-A][ao-B] * PQDEVIDE
                dp[gta][gao] %= DIV

ans = 0
print(dp)
for i in range(N - B):
    ans += dp[-1][i]
    ans %= DIV
print(ans)
                