import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, combinations_with_replacement
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
9999999999 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
fm = set()
fm.add(0)

for c in combinations_with_replacement(range(1, 10), 11):
    t = 1
    for i in c:
        t *= i
    fm.add(t)

ans = 0

for f in fm:
    if f + M <= N and f + M >= 1:
        S = str(f + M)
        t = 1
        for s in S:
            t *= int(s)
        if t == f:
            ans += 1

print(ans)
