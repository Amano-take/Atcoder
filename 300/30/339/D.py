import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10
..........
..........
..........
..........
....P.....
.....P....
..........
..........
..........
..........
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
grid = [list(input()) for _ in range(N)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dic = ddict(lambda:inf)
def __(x0, y0, x1, x2):
    return x0 * N**3 + y0 * N**2 + x1 * N + x2
P = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == "P":
            P.append((i, j))
dic[__(*P[0], *P[1])] = 0
que = deque([(P[0], P[1], 0)])
while que:
    (x, y, d) = que.popleft()
    for dx, dy in directions:
        x0, x1 = x[0], x[1]
        y0, y1 = y[0], y[1]
        if  0 <= x0 + dx < N and 0 <= x1 + dy < N and grid[x0 + dx][x1 + dy] != "#":
            next_x = (x0 + dx, x1 + dy)
        else:
            next_x = x
        if 0 <= y0 + dx < N and 0 <= y1 + dy < N and grid[y0 + dx][y1 + dy] != "#":
            next_y = (y0 + dx, y1 + dy)
        else:
            next_y = y
        if next_x[0] == next_y[0] and next_x[1] == next_y[1]:
            print(d + 1)
            exit()

        if dic[__(*next_x, *next_y)] is inf:
            dic[__(*next_x, *next_y)] = d + 1
            que.append((next_x, next_y, d + 1))
print(-1)