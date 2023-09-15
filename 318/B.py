import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
2
0 100 0 100
0 100 0 100
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
imo = [[0] * 101 for _ in range(101)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    imo[A][C] += 1
    imo[B][C] += -1
    imo[A][D] += -1
    imo[B][D] += 1
for i in range(101):
    for j in range(100):
        imo[i][j+1] += imo[i][j]

for i in range(101):
    for j in range(100):
        imo[j+1][i] += imo[j][i]

ans = 0

for i in range(101):
    for j in range(101):
        if imo[i][j] >= 1:
            ans += 1

print(ans)