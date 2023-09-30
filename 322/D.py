import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
4 3 5
5 3 0 2
3 1 2 3
3 2 4 0
1 0 1 4
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N, K, P = map(int, readline().split())
dp = [[10 ** 12] * ((P+1) ** K) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    C, *A = map(int, readline().split())
    for j in range((P+1) ** K):
        status = []
        temp = j
        for k in range(K):
            status.append(temp % (P+1))
            temp = temp // (P+1)
        for k in range(K):
            status[k] = min(P, status[k]+A[k])
        index = 0
        for k in range(K):
            index += status[k] * (P+1)**k
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][index] = min(dp[i+1][index], dp[i][j] + C)
if dp[-1][-1] != 10 ** 12:
    print(dp[-1][-1])
else:
    print("-1")
