import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
2
11
11
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
A = [list(map(int, list(readline().strip()))) for _ in range(N)]
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            ans[i][j] = A[1][0]
        elif i==0:
            ans[i][j] = A[i][j-1]
        elif j==N-1:
            ans[i][j] = A[i-1][j]
        elif i==N-1:
            ans[i][j] = A[i][j+1]
        elif j == 0:
            ans[i][j] = A[i+1][j]
        else:
            ans[i][j] = A[i][j]
for i in range(N):
    print("".join(map(str, ans[i])))