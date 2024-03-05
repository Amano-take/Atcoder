import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
20
0 0 76 100
70 99 95 100
10 64 96 91
12 37 99 66
63 93 65 95
16 18 18 67
30 47 88 56
33 6 38 8
37 19 40 68
4 56 12 84
3 16 92 78
39 24 67 96
46 1 69 57
40 34 65 65
20 38 51 92
5 32 100 73
7 33 92 55
4 46 97 85
43 18 57 87
15 29 54 74
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
masu = 1002
imos2 = [[0] * (masu+1) for _ in range(masu+1)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    ly = masu - ly 
    ry = masu - ry 
    imos2[lx][ry] += 1
    imos2[lx][ly] -= 1
    imos2[rx][ry] -= 1
    imos2[rx][ly] += 1

for i in range(masu):
    for j in range(masu-1):
        imos2[i][j+1] += imos2[i][j]



for i in range(masu-1):
    for j in range(masu):
        imos2[i+1][j] += imos2[i][j]
    
ans = [0] * (N+1)
for i in range(masu):
    for j in range(masu):
        ans[imos2[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])

