import sys
import io
import math
sys.setrecursionlimit(10**8)

_INPUT = """\
4
0 0 0 1 1 1
0 0 1 1 1 2
1 1 1 2 2 2
3 3 3 4 4 4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
X = [[] for _ in range(100)]
Y = [[] for _ in range(100)]
Z = [[] for _ in range(100)]

for i in range(N):
    X1, Y1, Z1, X2, Y2, Z2 = map(int, input().split())
    for x in range(X1+1, X2):
        X[x]
