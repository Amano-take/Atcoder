import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
e869120
atcoder
e869120
square1001
square1001
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
name = set()
for i in range(N):
    temp = input()
    if temp not in name:
        name.add(temp)
        print(i+1)