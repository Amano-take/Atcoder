import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
10000 27 7
1 3 4 6 7 8 9
"""
sys.stdin = io.StringIO(_INPUT)

#dfs

ANSDIV = 10**9 + 7

N, B, K = map(int, input().split())
C = list(map(int, input().split()))

dp = [[0] * B for _ in range(N)]
for c in C:
    dp[0][c] = 1
#dp[i+1][(r*10 + c[k])%B] += dp[i][r]

for n in range(N-1):
    for b in range(B):
        for c in C:
            dp[n+1][(b*10 + c)%B] += dp[n][b]
            dp[n+1][(b*10 + c)%B] %= ANSDIV
print(dp[N-1][0])