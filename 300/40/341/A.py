import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
"""
sys.stdin = io.StringIO(_INPUT)
input = lambda: sys.stdin.readline().strip()
N = int(input())
ans = []
for i in range(N):
    ans.append("1")
    ans.append("0")
ans.append("1")
print("".join(ans))