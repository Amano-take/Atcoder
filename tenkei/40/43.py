import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 3
1 1
3 3
..#
#.#
#..
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
def minus_one(x):
    return int(x) - 1
H, W = map(int, input().split())
sx, sy = map(minus_one, input().split())
sx, sy = sy, sx
gx, gy = map(minus_one, input().split())
gx, gy = gy, gx
grid = [input() for _ in range(H)]
dist = [inf] * (4*W*H)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
que = deque()
for i in range(4):
    dist[sy*(4*W) + sx*4 + i] = 0
    que.append((0, sx, sy, i))
while que:
    s, x, y, d = que.popleft()
    for i, (dx, dy) in enumerate(directions):
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] == '.':
            if i == d:
                if dist[ny*(4*W) + nx*4 + i] > s:
                    dist[ny*(4*W) + nx*4 + i] = s
                    que.appendleft((s, nx, ny, i))
            else:
                if dist[ny*(4*W) + nx*4 + i] > s + 1:
                    dist[ny*(4*W) + nx*4 + i] = s + 1
                    que.append((s + 1, nx, ny, i))
ans = inf
for i in range(4):
    ans = min(ans, dist[gy*(4*W) + gx*4 + i])
print(ans)
