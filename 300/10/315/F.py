import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
10
1 8
3 7
9 4
4 9
6 1
7 5
0 0
1 3
6 8
6 4
"""
sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline
N = int(input())
Climit = 26
dp = [[math.inf] * Climit for _ in range(N+1)]
P = [list(map(int, input().split())) for _ in range(N)]
def dis(i, j):
    xi, yi = P[i]
    xj, yj = P[j]
    return math.sqrt((xi - xj)**2 + (yi-yj)**2)
dp[0][0] = 0
for n in range(N):
    for c in range(min(n, Climit)):
        for t in range(n-c-1, n):
                dp[n][c] = min(dp[n][c], dp[t][c-(n-t-1)] + dis(t, n))
ans = dp[N-1][0]
for c in range(Climit):
    if c == 0:
        penalty = 0
    else:
        penalty = 2 ** (c-1)
    ans = min(ans, dp[N-1][c] + penalty)

print(ans)