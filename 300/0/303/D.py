import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1 3 3
AAaA
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
#dp[{0, 1}][I] = i文字目まで打っていてかつランプが点灯しているかどうか
X, Y, Z = map(int, readline().split())
S = readline().strip()
dp = [[inf] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0
dp[0][1] = Z
for i in range(1, len(S)+1):
    if S[i-1] == "A":
        dp[i][0] = min(dp[i-1][0] + Y, dp[i-1][1] + X + Z, dp[i-1][1] + Z + Y)
        dp[i][1] = min(dp[i-1][0] + Y + Z, dp[i-1][1] + X, dp[i-1][0] + Z + Y)
    else:
        dp[i][0] = min(dp[i-1][0] + X, dp[i-1][1] + Z + X,  dp[i-1][1] + Y + Z)
        dp[i][1] = min(dp[i-1][0] + X + Z, dp[i-1][1] + Y, dp[i-1][0] + Z + Y)


print(min(dp[len(S)][0], dp[len(S)][1]))