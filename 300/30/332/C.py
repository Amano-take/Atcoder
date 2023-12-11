import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 1
112022
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
S = input()
m = M
l = 0
ans = 0
for s in S:
    if s == "0":
        m = M
        l = 0
    elif s == "1":
        if m == 0:
            l += 1
            ans = max(ans, l)
        else:
            m -= 1
    elif s == "2":
        l += 1
        ans = max(ans, l)
print(ans)