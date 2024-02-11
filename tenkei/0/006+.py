import sys
import io
sys.setrecursionlimit(10**8)



N, K = map(int, input().split())
S = input()
res = [[N] * 26 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(26):
        res[i][j] = res[i+1][j]

    res[i][ord(S[i]) - ord('a')] = i

ans = ''
j = -1
for i in range(K):
    for ordc in range(26):
        k = res[j+1][ordc]

        if N - k >= K - i:
            ans += chr(ord('a') + ordc)
            j = k
            break

print(ans)