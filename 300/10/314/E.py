import sys
import io
import random
sys.setrecursionlimit(10**8)
_INPUT="""\
3 14
100 2 5 9
50 4 1 2 4 8
70 5 2 4 2 8 8
"""
sys.stdin=io.StringIO(_INPUT)
readline = sys.stdin.readline

N, M = map(int, input().split())
roulett = []
dp = [10**8] * (M+1)
dp[0] = 0

for i in range(N):
    c, p, *num = map(int, readline().split())
    cand = []
    for n in num:
        if n != 0:
            cand.append(n)
    roulett.append((c * len(num) / len(cand) , cand))


for i in range(1, M+1):
    for c, deme in roulett:
        total = 0
        for d in deme:
            total += dp[max(0, i-d)] / len(deme)
        dp[i] = min(dp[i], total + c)
print(dp[-1])
