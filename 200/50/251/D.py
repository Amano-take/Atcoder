import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

ans = []
for i in range(1, 100):
    ans.append(i)
for i in range(1, 100):
    ans.append(i * 100)
    ans.append(i * 100 * 100)
ans.sort()

print(len(ans))
print(*ans)