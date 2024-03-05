import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1 10
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W = map(int, input().split())
if H == 1 or W == 1:
    print(max(H, W))
    exit()
print((H // 2 if H % 2 == 0 else (H // 2 + 1)) * ((W // 2) if W % 2 == 0 else (W // 2 + 1)))