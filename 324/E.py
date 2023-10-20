import sys
import io
from collections import defaultdict as ddict
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
3 6
3 5 6
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, X = map(int, readline().split())
T = list(map(int, readline().split()))
DIV = 998244353
dp = [0] * (X + max(T))
divideN = pow(N, -1, DIV)
dp[0] = divideN
cash = ddict(int)
for i in range(X):
    if dp[i] != 0:
        for t in T:
            dp[i+t] += (dp[i] * divideN)%DIV
ans = 0
for i in range(T[0]):
    ans += dp[X - i]
    ans %= DIV
print(ans)

