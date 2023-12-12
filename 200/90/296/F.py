import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
1 2 3 2 1
3 2 2 1 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Aindex = ddict(list)
Bindex = ddict(list)
for i in range(N):
    Aindex[As[i]].append(i)
    Bindex[Bs[i]].append(i)

while True:
    
