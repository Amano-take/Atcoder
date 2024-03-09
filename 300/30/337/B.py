import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
AC
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
S = input()
t = []
for s in S:
    t.append(ord(s))

for i in range(1, len(S)):
    if t[i] < t[i-1]:
        print("No")
        exit()
print("Yes")