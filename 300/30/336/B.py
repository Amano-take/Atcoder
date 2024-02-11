import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2025
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
ans = 0
N = int(input())
while True:
    if N % 2 == 1:
        break
    else:
        ans += 1
        N //= 2
print(ans)