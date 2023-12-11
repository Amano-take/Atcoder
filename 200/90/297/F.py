import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import time
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1000 1000 10000
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
DIV = 998244353
H, W, K = map(int, input().split())
factorial = [1]
DIVfactorial = [1]
for i in range(1, H*W+1):
    factorial.append(factorial[-1] * i % DIV)
for i in range(1, H*W+1):
    DIVfactorial.append(DIVfactorial[-1] * pow(i, -1, DIV) % DIV)

def comb(n, r):
    return factorial[n] * DIVfactorial[r] * DIVfactorial[n-r] % DIV
hwCk = comb(H*W, K)
invhwCk = pow(hwCk, -1, DIV)

dp = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        N = (i+1) * (j+1)
        if N < K:
            continue
        else:
            dp[i][j] = comb(N, K) * invhwCk  % DIV
ans = 0

for i in range(H):
    for j in range(W):
        if i > 1 and j > 1:
            realprob = dp[i][j] - 2*dp[i-1][j] - 2*dp[i][j-1] + 4*dp[i-1][j-1] + dp[i-2][j] + dp[i][j-2] - 2*dp[i-2][j-1] - 2*dp[i-1][j-2] + dp[i-2][j-2]
        elif i > 1 and j > 0:
            realprob = dp[i][j] - 2*dp[i-1][j] - 2*dp[i][j-1] + 4*dp[i-1][j-1] + dp[i-2][j]- 2*dp[i-2][j-1] 
        elif i > 0 and j > 1:
            realprob =dp[i][j] - 2*dp[i-1][j] - 2*dp[i][j-1] + 4*dp[i-1][j-1] + dp[i][j-2]- 2*dp[i-1][j-2] 
        elif i > 0 and j > 0:
            realprob =  dp[i][j] - 2*dp[i-1][j] - 2*dp[i][j-1] + 4*dp[i-1][j-1]
        elif i > 1:
            realprob = dp[i][j] - 2 * dp[i-1][j] + dp[i-2][j]
        elif j > 1:
            realprob = dp[i][j] - 2 * dp[i][j-1] + dp[i][j-2]
        elif i > 0:
            realprob = dp[i][j] - 2 * dp[i-1][j] 
        elif j > 0:
            realprob = dp[i][j] - 2 * dp[i][j-1]
        else:
            realprob = dp[i][j]
        realprob %= DIV
        ans += realprob * (i+1) * (j+1) * (H - i) * (W - j)% DIV
        ans %= DIV
print(ans)

