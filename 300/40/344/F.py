import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
1 2 3
3 1 2
2 1 1
1 2
4 3
4 2
1 5 7
5 3 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
Pgrid = [list(map(int, input().split())) for _ in range(N)]
Rgrid = [list(map(int, input().split())) for _ in range(N)]
Qgrid = [list(map(int, input().split())) for _ in range(N)]



