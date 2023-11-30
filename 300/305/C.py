import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
5 6
......
...#..
..##.
..##..
......
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
H, W = map(int, readline().split())
board  = [ list(input()) for _ in range(H)]
count = []
for y, line in enumerate(board):
    count.append(line.count("#"))
width = 0
for y, c in enumerate(count):
    if c > width:
        width = c
        target = y
l = board[target]

for y, line in enumerate(board):
    if count[y] == width - 1:
        for x in range(W):
            if l[x] != line[x]:
                print(y+1, x+1)
