import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
20230322
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
sum = 0
dd = ddict(int)
dd[sum] += 1
S = list(input())
for s in S:
    sum ^= 1 << (int(s))
    dd[sum] += 1

ans = 0
for i in dd.values():
    ans += i * (i - 1) // 2

print(ans)