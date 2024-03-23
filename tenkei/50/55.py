import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, combinations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 7 1
1 2 3 4 5 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, P, Q = map(int, input().split())
A = list(map(lambda x: int(x) % P, input().split()))
dic = ddict(int)

ans = 0
for a, b, c, d, e in combinations(A, 5):
    if a * b % P * c % P * d % P * e % P == Q:
        ans += 1
print(ans)