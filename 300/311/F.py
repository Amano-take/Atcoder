import sys
import io
import math

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 5
....#
...#.
..#..
.#.#.
#...#
"""
sys.stdin = io.StringIO(_INPUT)
readline = lambda: sys.stdin.readline().strip()
DIV = 998244353
N, M = map(int, readline().split())
grid = [list(readline()) for _ in range(N)]
column_high = []
temp = N - 1
for c in range(M):
    temp += 1
    for i in range(N):
        if grid[i][c] == "#":
            temp = min(temp, i)
            break
        else:
            temp = N
    column_high.append(temp)

dp = [[0] * (N + 1) for i in range(M + 1)]
# dp[m][n] ... m段目までで、上からn番目までが白であるような場合の数
for r in range(column_high[0] + 1):
    dp[1][r] = 1
for c in range(1, M):
    ch = column_high[c]
    for r in range(ch, -1, -1):
        if r == ch:
            dp[c + 1][r] = sum(dp[c][max(0, r - 1) : N + 1])
        else:
            if r == 0:
                dp[c + 1][r] = dp[c + 1][r + 1]
            else:
                dp[c + 1][r] = dp[c + 1][r + 1] + dp[c][r - 1]
        dp[c + 1][r] = dp[c + 1][r] % DIV
print(sum(dp[M]) % DIV)
