import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
from sortedcontainers import SortedList
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
1 2
1 1
2 3
3 1
3 2
3 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
min = 0
max = 1
sl = SortedList()
N = int(input())
for i in range(N):
    t, *x = map(int, input().split())
    if t == 2:
        sl.add((max, x[0]))
        max += 1
    elif t == 1:
        sl.add((min, x[0]))
        min -= 1
    else:
        print(sl[x[0]-1][1])
