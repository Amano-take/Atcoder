#ruisekiwa

import sys
import io
sys.setrecursionlimit(10**8)



N = int(input())
memo = [[0] * (N+1) for _ in range(2)]

for i in range(N):
    c, p = map(int, input().split())
    memo[0][i+1] = memo[0][i]
    memo[1][i+1] = memo[1][i]
    if c == 1:
        memo[0][i+1] += p
    else:
        memo[1][i+1] += p

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(str(memo[0][r] - memo[0][l-1]) + " " + str(memo[1][r] - memo[1][l-1]))