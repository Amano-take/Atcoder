import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import matplotlib.pyplot as plt
import random 
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10
72 7
54 25
97 48
37 47
34 54
4 16
62 1
59 22
99 73
34 75
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

XY.sort()
# 閉方を作る
stack = []
for x, y in XY:
    while True:
        if len(stack) < 2:
            stack.append((x, y))
            break
        x1, y1 = stack[-1]
        x2, y2 = stack[-2]
        if (x1-x2)*(y-y2) - (y1-y2)*(x-x2) >= 0:
            stack.pop()
        else:
            stack.append((x, y))
            break

for x, y in XY[::-1]:
    while True:
        if len(stack) < 2:
            stack.append((x, y))
            break
        x1, y1 = stack[-1]
        x2, y2 = stack[-2]
        if (x1-x2)*(y-y2) - (y1-y2)*(x-x2) >= 0:
            stack.pop()
        else:
            stack.append((x, y))
            break

fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(XY)):
    ax.plot(XY[i][0], XY[i][1], 'o', color='b')
for i in range(len(stack)-1):
    ax.plot([stack[i][0], stack[i+1][0]], [stack[i][1], stack[i+1][1]], 'r')
plt.show()