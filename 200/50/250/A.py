import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4
2 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

H, W = map(int, input().split())
R, C = map(int, input().split())

plus = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = 0

for a, b in plus:
    if R + a <= H and R + a >= 1 and C + b <= W and C + b >= 1:
        ans += 1

print(ans)