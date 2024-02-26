import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
3 -5 7 -4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
s = 0
ans = 0
As = list(map(int, input().split()))
for a in As:
    s += a
    ans = min(ans, s)
print(-ans + s)