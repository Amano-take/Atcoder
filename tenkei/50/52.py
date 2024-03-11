import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2
1 2 3 5 7 11
4 6 8 9 10 12
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
DIV = 10 ** 9 + 7
N = int(input())
ans = 1
for i in range(N):
    *deme,  = map(int, input().split())
    ans *= sum(deme)
    ans %= DIV
print(ans)