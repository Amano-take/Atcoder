import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 1 1
1 2
4 1
1 4
1 4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M, K = map(int, input().split())
takahashi = [list(map(int, input().split())) for _ in range(N)]
aoki = [list(map(int, input().split())) for _ in range(M)]
