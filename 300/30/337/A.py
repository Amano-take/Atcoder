import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
10 2
10 1
10 2
3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
a, b = 0, 0
for i in range(N):
    x, y = map(int, input().split())
    a += x
    b += y
if a > b:
    print("Takahashi")
elif a == b:
    print("Draw")
else:
    print("Aoki")