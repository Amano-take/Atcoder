import sys
import io
sys.setrecursionlimit(10**8)


ANSDEV = 10**9 + 7

N = int(input())
S = input()

dp = [[0] * 7 for _ in range(N)]

flag = True
atcoder = ['a', 't', 'c', 'o', 'd', 'e']
for i in range(N-1, -1, -1):
    if not flag:
        dp[i] = dp[i+1].copy()
        if S[i] == 'r':
            dp[i][0] += 1
            continue
        for j, s in enumerate(atcoder):
            if S[i] == s:
                dp[i][6-j] += dp[i+1][5-j]
                dp[i][6-j] %= ANSDEV
        

    if S[i] == 'r' and flag:
        flag = False
        dp[i][0] = 1

print(dp[0][6])