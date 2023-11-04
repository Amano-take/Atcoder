import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
4
1 1 0 2
MEEX
"""
sys.stdin = io.StringIO(_INPUT)
readline = lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, readline().split()))
S = list(readline())
Ms = [[0] * (N+1) for _ in range(3)]
Xs = [[0] * (N+1) for _ in range(3)]
def MEX(i, j, k):
    for a in range(4):
        if a not in [i, j, k]:
            return a
        
for i in range(N):
    for j in range(3):
        Ms[j][i+1] = Ms[j][i]
        if j == As[i] and S[i] == "M":
            Ms[j][i+1] += 1

for i in range(N, 0, -1):
    for j in range(3):
        Xs[j][i-1] = Xs[j][i]
        if S[i-1] == "X" and As[i-1] == j:
            Xs[j][i-1] += 1
ans = 0
for i, s in enumerate(S):
    if s == "E":
        n = As[i]
        for k in range(3):
            for j in range(3):
                ans += MEX(n, k, j) * Ms[k][i] * Xs[j][i+1]
print(ans)