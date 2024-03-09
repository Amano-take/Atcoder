import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
4 1 -1 5 3 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
graph = ddict(int)
for a in range(N):
    if As[a] == -1:
        start = a + 1
    else:
        graph[As[a]] = a + 1

line = [start]
for i in range(N-1):
    line.append(graph[line[-1]])
print(*line)