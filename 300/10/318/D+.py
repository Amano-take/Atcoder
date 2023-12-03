import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
10
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
# 計算・出力
sumZ = 0
sumTakahashi = 0
costreward = []
for _ in range(N):
    X, Y, Z = map(int, readline().split())
    sumZ += Z
    if X < Y:
        costreward.append((( Y - X + 1) // 2, Z))
    else:
        sumTakahashi += Z

totalreward = (sumZ + 1) // 2 - sumTakahashi
if totalreward <= 0:
    print("0")
    exit()

dp = [10**12]*(totalreward+1)
dp[0] = 0


for i in range(len(costreward)):
    c, r = costreward[i]
    for j in range(totalreward, -1, -1):
        if j+r > totalreward:
            dp[totalreward] = min(dp[totalreward], dp[j]+c)
        else:
            dp[j+r] = min(dp[j+r], dp[j]+c)
print(dp[-1])