import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
3 1 4 1 5 9
2 7 1 8 2 8
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

def mex(s):
    for i in range(2000):
        if i not in s:
            return i
    return 2000

N = int(input())
Ws = list(map(int, input().split()))
Bs = list(map(int, input().split()))
grandy = ddict(int)
for i in range(51):
    for j in range(1326):
        if i == 0 and (j == 0 or j == 1):
            grandy[(i, j)] = 0
            continue
        
        s = set()
        if i > 0:
            s.add(grandy[(i-1, j+i)])
        if j > 1:
            k = j // 2
            for l in range(1, k+1):
                s.add(grandy[(i, j-l)])
        grandy[(i, j)] = mex(s)



g = []
for w, b in zip(Ws, Bs):
    g.append(grandy[(w, b)])

xorsum = 0
for i in g:
    xorsum ^= i
if xorsum == 0:
    print("Second")
else:
    print("First")