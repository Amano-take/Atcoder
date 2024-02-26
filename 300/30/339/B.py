import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W, N = map(int, input().split())
grid = [["."] * W for _ in range(H)]
start = (0, 0)
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir = 0
for _ in range(N):
    if grid[start[1]][start[0]] == ".":
        dir = (dir + 1) % 4
        grid[start[1]][start[0]] = "#"
    elif grid[start[1]][start[0]] == "#":
        dir = (dir - 1) % 4
        grid[start[1]][start[0]] = "."
    start = ((start[0] + directions[dir][0]) % W, (start[1] + directions[dir][1]) % H)
for row in grid:
    print("".join(row))

    