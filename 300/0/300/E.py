import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
6
"""
MOD = 998244353
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(readline())
#prime factorization
p, q, r = 0, 0, 0
while N % 2 == 0:
    p += 1
    N //= 2
while N % 3 == 0:
    q += 1
    N //= 3
while N % 5 == 0:
    r += 1
    N //= 5
if N != 1:
    print(0)
    exit()
#dp[i][j][k] 2**i * 3**j * 5**kを経験する確率
dp = [[[0] * (r + 1) for _ in range(q + 1)] for _ in range(p + 1)]
dp[0][0][0] = 1
onedividefive = pow(5, -1, MOD)

#dice
for i in range(p+1):
    for j in range(q + 1):
        for k in range(r + 1):
            if i > 0:
                dp[i][j][k] += (dp[i - 1][j][k] * onedividefive) % MOD
            if j > 0:
                dp[i][j][k] += (dp[i][j-1][k] * onedividefive) % MOD
            if k > 0:
                dp[i][j][k] += (dp[i][j][k-1] * onedividefive) % MOD
            if i > 0 and j > 0:
                dp[i][j][k] += (dp[i - 1][j - 1][k] * onedividefive) % MOD
            if i > 1:
                dp[i][j][k] += (dp[i - 2][j][k] * onedividefive) % MOD
            dp[i][j][k] %= MOD
print(dp[p][q][r])