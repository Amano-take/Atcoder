from collections import deque
import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

ans = 0
N = int(input())
dp = [[0] * (N+1) for _ in range(2)]
for i in range(N):
    X, Y = map(int, readline().split())
    if X == 0:
        dp[0][i+1] = max(dp[0][i], dp[0][i] + Y, dp[1][i] + Y)
        dp[1][i+1] = dp[1][i]
    else:
        dp[0][i+1] = dp[0][i]
        dp[1][i+1] = max(dp[1][i], dp[0][i] + Y)

print(max(dp[0][-1], dp[1][-1]))