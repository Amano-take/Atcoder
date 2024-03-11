import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, combinations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 12
3 3 3 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, W = map(int, input().split())
A = list(map(int, input().split()))

s = set()
for num in range(1, 4):
    for *a, in combinations(A, num):
        s.add(sum(a))

ans = 0
for i in s:
    if i <= W:
        ans += 1

print(ans)