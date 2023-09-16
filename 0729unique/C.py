import sys
import io
import math
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10**8)



N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

#絶対にありえない答えを使用！！
ans = 10 ** 9 + 10
for i in range(N):
    j = bisect_left(B, A[i])
    if i+1 >= M - j:
        ans = min(ans, A[i])
        break

for i in range(M):
    kaite = bisect_left(B, B[i]+1)
    j = bisect_right(A, B[i]+1)
    if M - kaite <= j:
        ans = min(ans, B[i]+1)
        break

print(ans)

