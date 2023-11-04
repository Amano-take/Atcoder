from collections import defaultdict
import sys
import io
import math

sys.setrecursionlimit(10**8)
_INPUT = """\
7
1 10 100 1000 10000 100000 1000000
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
DIV = 998244353
mask = (1 << 10) - 1
deme = list(map(int, readline().split()))
dp = [[0] * (1 << 10) for _ in range(N + 1)]
dp[0][0] = 1
for n in range(N):
    for iset, p in enumerate(dp[n]):
        if deme[n] > 10:
            dp[n + 1][iset] += (deme[n] - 10) * p * pow(deme[n], -1, DIV)
            dp[n + 1][iset] %= DIV
        for d in range(1, min(deme[n] + 1, 11)):
            nextset = iset | (1 << (d - 1))
            for shift in range(10):
                if (iset >> shift) & 1 == 1:
                    nextset = nextset | ((1 << (shift + d)) & mask)
            dp[n + 1][nextset] += p * pow(deme[n], -1, DIV)
            dp[n + 1][nextset] %= DIV

ans = 0
for i in range(1 << 9, 1 << 10):
    ans += dp[N][i]
    ans %= DIV
print(ans)
