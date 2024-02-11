import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, A, B = map(int, input().split())

ans = [["."] * (N*B) for _ in range(N*A)]

for i in range(N):
    for j in range(N):
        if j % 2 + i % 2 == 1:
            for k in range(A):
                for l in range(B):
                    ans[i*A+k][j*B+l] = "#"

for an in ans:
    print("".join(an))