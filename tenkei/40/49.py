import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")

sys.setrecursionlimit(10**8)
_INPUT = """\
9 11
10 2 7
100 1 6
1 2 8
39 4 5
62 3 4
81 1 3
55 8 8
91 5 5
14 8 9
37 5 5
41 7 9
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
A = []
for i in range(M):
    c, l, r = map(int, input().split())
    A.append((r-l, c, l))
A.sort()


