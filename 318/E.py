import sys
import io
import itertools
from collections import deque

sys.setrecursionlimit(10**8)
_INPUT = """\
4 3
S..
.<.
.>.
..G
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

H, W = map(int, readline().split())
mapHW = [list(readline().strip()) for _ in range(H)]
canThrough = [[True] * W for _ in range(H)]
human = ["<", "v", ">", "^"]
directionX = [-1, 0, 1, 0]
directionY = [0, 1, 0, -1]
start = (0, 0)
goal = (0, 0)

for h, w in itertools.product(range(H), range(W)):
    box = mapHW[h][w]
    if box == "#":
        canThrough[h][w] = False
        continue
    
    if box == "S":
        start = (h, w)
        continue
    
    if box == "G":
        goal = (h, w)

    for i, mark in enumerate(human):
        if box == mark:
            dx = directionX[i]
            dy = directionY[i]
            itemx = w
            itemy = h
            canThrough[h][w] = False
            while itemx + dx < W and itemx + dx >= 0 and itemy+dy < H and itemy+dy >= 0:
                itemx += dx
                itemy += dy
                if mapHW[itemy][itemx] == ".":
                    canThrough[itemy][itemx] = False
                else:
                    break

queue = deque()
queue.append(start)
Ans = [[-1] * W for _ in range(H)]
Ans[start[0]][start[1]] = 0

while len(queue) != 0:
    py, px = queue.popleft()
    c = Ans[py][px]
    for i in range(4):
        dx = directionX[i]
        dy = directionY[i]
        if px+dx < W and px+dx >= 0 and py+dy < H and py+dy >= 0:
            if canThrough[py+dy][px+dx] and Ans[py+dy][px+dx] == -1:
                Ans[py+dy][px+dx] = c+1
                queue.append((py+dy, px+dx))


print(Ans[goal[0]][goal[1]])

