import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2 2000 500
1000 1
100 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, S, K = map(int, input().split())
price = 0
for i in range(N):
    x, y = map(int, input().split())
    price += x * y
if price >= S:
    print(price)
else:
    print(price + K)