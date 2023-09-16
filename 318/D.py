import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
2
3 1 3
1 2 1
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N = int(input())
sumZ = 0
sumTakahashi = 0
cost = []
reward = []
for _ in range(N):
    X, Y, Z = map(int, readline().split())
    sumZ += Z
    if X < Y:
        cost.append(( Y - X + 1) // 2)
        reward.append(Z)
    else:
        sumTakahashi += Z

totalreward = (sumZ + 1) // 2 - sumTakahashi
if totalreward <= 0:
    print("0")
    exit()


dp = [[math.inf] * (totalreward + 1) for _ in range(len(cost) + 1)]
dp[0][0] = 0

for selection in range(len(cost)):
    c = cost[selection]
    r = reward[selection]
    for rsel in range(totalreward + 1):
        dp[selection+1][min(rsel + r, totalreward)] = min(dp[selection][rsel]+c, dp[selection+1][min(rsel+r, totalreward)])
        dp[selection+1][rsel] = min(dp[selection+1][rsel], dp[selection][rsel])
print(dp[-1][-1])