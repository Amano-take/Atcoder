import itertools
import sys
import io
import math

sys.setrecursionlimit(10**8)
_INPUT = """\
3 3
###
...
...
3 3
#..
#..
#..
3 3
..#
..#
###
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
Ha, Wa = map(int, readline().split())
grida = [list(readline().strip()) for _ in range(Ha)]
Hb, Wb = map(int, readline().split())
gridb = [list(readline().strip()) for _ in range(Hb)]
Hx, Wx = map(int, readline().split())
gridx = [list(readline().strip()) for _ in range(Hx)]
# left, right, top, bottom


def lrtb(grid):
    row = []
    col = []
    h, w = len(grid), len(grid[0])
    for i in range(w):
        for j in range(h):
            if grid[j][i] == "#":
                col.append(i)
                row.append(j)
    return [min(col), max(col), min(row), max(row)]

lrtba = lrtb(grida)
lrtbb = lrtb(gridb)
lrtbx = lrtb(gridx)
ax_x = []
bx_x = []
ax_y = []
bx_y = []
for i in range(-10, 11):
    if lrtba[0] + i >= lrtbx[0] and lrtba[1] + i <= lrtbx[1]:
        ax_x.append(i)
    if lrtbb[0] + i >= lrtbx[0] and lrtbb[1] + i <= lrtbx[1]:
        bx_x.append(i)
    if lrtba[2] + i >= lrtbx[2] and lrtba[3] + i <= lrtbx[3]:
        ax_y.append(i)
    if lrtbb[2] + i >= lrtbx[2] and lrtbb[3] + i <= lrtbx[3]:
        bx_y.append(i)

for ax, ay in itertools.product(ax_x, ax_y):
    gridy = [[0] * Wx for _ in range(Hx)]
    for ar, ac in itertools.product(range(Ha), range(Wa)):
        if grida[ar][ac] == "#" and gridx[ar + ay][ac + ax] == ".":
            break
        elif grida[ar][ac] == "#":
            gridy[ar + ay][ac + ax] = 1
    else:
        for bx, by in itertools.product(bx_x, bx_y):
            for br, bc in itertools.product(range(Hb), range(Wb)):
                if gridb[br][bc] == "#" and gridx[br + by][bc + bx] == ".":
                    break
                elif gridb[br][bc] == "#":
                    gridy[br + by][bc + bx] = 1
            else:
                for xr, xc in itertools.product(range(Hx), range(Wx)):
                    if gridx[xr][xc] == "#" and gridy[xr][xc] == 0:
                        break
                else:
                    print("Yes")
                    exit()
print("No")
