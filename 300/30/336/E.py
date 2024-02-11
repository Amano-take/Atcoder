n = input()
ans = 0

#sum of digits
for d in range(1,127):
    n = n
    L = len(n)
    dp = [[[[0]*2 for _1 in range(d+1)] for _2 in range(d)] for _3 in range(L+1)]

    dp[0][0][0][0] = 1
    #digit dp
    #digit, mod, sum
    for i in range(L):
        for j in range(d):
            for k in range(d+1):
                for x in range(10):
                    if k+x > d:
                        break
                    if x == int(n[i]):
                        dp[i+1][(10*j+x)%d][k+x][0] += dp[i][j][k][0]
                    if x < int(n[i]):
                        dp[i+1][(10*j+x)%d][k+x][1] += dp[i][j][k][0]
                    dp[i+1][(10*j+x)%d][k+x][1] += dp[i][j][k][1]
    ans += dp[L][0][-1][0]+dp[L][0][-1][1]

print(ans)