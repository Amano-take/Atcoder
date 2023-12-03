import sys
import io
import math

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1
100
"""
sys.stdin = io.StringIO(_INPUT)
readline = lambda: sys.stdin.readline().strip()
N = int(input())
Ps = list(map(int, readline().split()))
dp = [[-inf] * (N + 1) for _ in range(N + 1)]

zerodotnine = [0] * (N + 1)
zerodotnine[0] = 1
plus = 0.9
for i in range(N):
    zerodotnine[i + 1] += zerodotnine[i] + plus
    plus *= 0.9

for i in range(N):
    for j in range(N + 1):
        if j > i + 1:
            break
        dp[i + 1][j] = dp[i][j]
        if j != 0 and j != 1 and dp[i][j - 1] != 0:
            dp[i + 1][j] = max(
                dp[i + 1][j],
                (
                    (dp[i][j - 1] + 1200 / math.sqrt(j - 1)) * zerodotnine[j - 2] * 0.9
                    + Ps[i]
                )
                / zerodotnine[j - 1]
                - 1200 / math.sqrt(j),
            )
        elif j == 1:
            dp[i + 1][j] = max(dp[i + 1][j], Ps[i] - 1200 / math.sqrt(1))
print(max(dp[N]))
