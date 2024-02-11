MOD = 1000000007
T = 'atcoder'

# a に b を足して MOD をとる関数
def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a

N = int(input())
S = input()

# DP テーブル
dp = [[0]*(len(T)+1) for _ in range(N+1)]

# 初期条件<= kore
dp[0][0] = 1

# ループ
for i in range(N):
    for j in range(len(T)+1):
        # S[i] を選ばない場合
        dp[i+1][j] = add(dp[i+1][j], dp[i][j])

        # S[i] を選ぶ場合
        if j < len(T) and S[i] == T[j]:
            dp[i+1][j+1] = add(dp[i+1][j+1], dp[i][j])

print(dp[N][len(T)])