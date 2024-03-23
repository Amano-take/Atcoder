import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 3
1 2 3
2 3 1
1 2 -1
1 3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, Q = map(int, input().split())
A = list(map(int, input().split()))
E = []
for i in range(1, N):
    E.append(A[i-1] - A[i])

ans = sum(abs(e) for e in E)

for q in range(Q):
    l, r, v = map(int, input().split())
    l -= 2
    r -= 1
    if l >= 0:
        ans -= abs(E[l])
        E[l] -= v
        ans += abs(E[l])
    if r <= N - 2:
        ans -= abs(E[r])
        E[r] += v
        ans += abs(E[r])
    print(ans)