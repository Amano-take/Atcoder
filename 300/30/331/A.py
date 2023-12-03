import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
12 30
2023 12 30
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

M, D = map(int, input().split())
y, m, d = map(int, input().split())
d += 1
if d > D:
    d = 1
    m += 1

if m > M:
    m = 1
    y += 1

print(y, m, d) 