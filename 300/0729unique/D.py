import sys
import io
import math
sys.setrecursionlimit(10**8)

ANSDIV = 998244353

S = input()
lenlen = len(S) // 2 + 1
dp = [[0] * lenlen for _ in range(len(S) + 1)]
dp[0][0] = 1

##

for i, s in enumerate(S):
    if s == '(' or s == '?':
        for j in range(1, lenlen):
            dp[i+1][j] += dp[i][j-1]
            dp[i+1][j] %= ANSDIV
    if s == ')' or s == '?':
        for j in range(lenlen - 1):
            dp[i+1][j] += dp[i][j+1]
            dp[i+1][j] %= ANSDIV

print(dp[len(S)][0])


