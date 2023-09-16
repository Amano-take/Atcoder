import sys
import io
sys.setrecursionlimit(10**8)



H, W = map(int, input().split())
sumH = [0] * W
sumW = [0] * H
A = [[0] * W for _ in range(H)]
for i in range(H):
    l = map(int, input().split())
    sum = 0
    for j, v in enumerate(l):
        A[i][j] = v
        sum += v
        sumH[j] += v
    sumW[i] = sum


sumHW = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        sumHW[i][j] = sumW[i] + sumH[j] - A[i][j]

for v in sumHW:
    print(*v)