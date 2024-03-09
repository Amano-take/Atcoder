import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
2
1
0
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

stack = []
while True:
    a = int(input())
    if a == 0:
        stack.append(0)
        while stack:
            print(stack.pop())
        break

    else:
        stack.append(a)
