import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
1 20
1 30
2 1
1 40
2 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
Q = int(input())
A = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        A.append(x)
    elif t == 2:
        print(A[-x])