import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 300 500
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
K, G, M = map(int, input().split())
g, m = 0, 0
while K > 0:
    if g == G:
        g = 0
        K -= 1
    elif m == 0:
        m = M
        K -= 1
    else:
        water = min(m, G- g)
        m -= water
        g += water
        K -= 1
print(g, m)