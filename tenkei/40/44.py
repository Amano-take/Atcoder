import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = ddict(int)
for i, a in enumerate(A):
    dic[i] = a 

rotation = 0
for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 2:
        rotation += 1
        rotation %= N
    elif t == 1:
        x -= 1 + rotation
        y -= 1 + rotation
        x %= N
        y %= N
        dic[x], dic[y] = dic[y], dic[x]
    else:
        x -= 1 + rotation
        x %= N
        print(dic[x])
