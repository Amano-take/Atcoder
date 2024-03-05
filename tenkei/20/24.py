import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2 5
1 3
2 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

for i in range(N):
    K -= abs(As[i] - Bs[i])

if K < 0 or K % 2 == 1:
    print("No")
else:
    print("Yes")