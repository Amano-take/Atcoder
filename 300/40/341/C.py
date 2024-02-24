import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 7 5
LULDR
#######
#...#.#
##...##
#.#...#
#...#.#
#######
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

H, W, N = map(int, input().split())
T = input()
grid = [input() for _ in range(H)]
start = (0, 0)
path = [(0, 0)]
for s in T:
    if s == "L":
        start = (start[0], start[1]-1)
    elif s == "R":
        start = (start[0], start[1]+1)
    elif s == "U":
        start = (start[0]-1, start[1])
    elif s == "D":
        start = (start[0]+1, start[1])
    path.append(start)
def check(x, y):
    for p in path:
        if grid[p[0]+x][p[1]+y] == "#":
            return False
    return True

ans = 0
for w in range(W):
    for h in range(H):
        if check(h, w):
            ans += 1

print(ans)
