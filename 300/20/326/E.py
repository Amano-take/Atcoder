import sys
import io
import math

sys.setrecursionlimit(10**8)
_INPUT = """\
3
3 2 6
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
DIV = 998244353
N = int(input())
francNDIV = pow(N, -1, DIV)
A = list(map(int, readline().split()))
dp = [0] * N
calsumA = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    calsumA[i] = calsumA[i + 1] + A[i]
dpgoukei = 0
for i in range(N - 1, -1, -1):
    dp[i] = (francNDIV * (calsumA[i] + dpgoukei)) % DIV
    dpgoukei += dp[i]
    dpgoukei %= DIV
print(dp[0])