import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
2 1 3
3
2 3
1 2
1 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
dic = ddict(int)
P = list(map(int, input().split()))
for i, p in enumerate(P):
    dic[p] = i
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    if dic[a] > dic[b]:
        print(b)
    else:
        print(a)