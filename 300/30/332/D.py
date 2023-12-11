import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, permutations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
1 3 2 5 4
11 13 12 15 14
6 8 7 10 9
16 18 17 20 19
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W = map(int, input().split())
gridA = [list(map(int, input().split())) for _ in range(H)]
gridB = [list(map(int, input().split())) for _ in range(H)]
def issame(P, Q):
    for i in range(H):
        for j in range(W):
            if gridA[P[i]][Q[j]] != gridB[i][j]:
                return False
    return True
def inversion_number(P):
    ans = 0
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if P[i] > P[j]:
                ans += 1
    return ans
ans = inf
for P in permutations(range(H)):
    for Q in permutations(range(W)):
        if issame(P, Q):
            ans = min(ans, inversion_number(P) + inversion_number(Q))
if ans is inf:
    print(-1)
else:
    print(ans)