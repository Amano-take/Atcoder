import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
5 7 0 3
2 2
4 3
5 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
for i in range(N-1):
    a, b = map(int, input().split())
    if As[i] >= a:
        As[i+1] += (As[i] // a) * b
        As[i] %= a

print(As[-1])

