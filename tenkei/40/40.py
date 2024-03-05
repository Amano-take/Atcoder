import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)






_INPUT = """\
5 5
5 2 10 3 6
1 3
1 3
0
1 5
0
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, W = map(int, input().split())
As = list(map(lambda x: int(x) - W, input().split()))
