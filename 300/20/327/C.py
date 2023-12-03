import itertools
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
grid = [list(readline().split()) for _ in range(9)]
for r in range(9):
    checker = set(grid[r])
    if len(checker) != 9:
        print("No")
        exit()

for c in range(9):
    checker = set()
    for r in range(9):
        checker.add(grid[r][c])
    if len(checker) != 9:
        print("No")
        exit()

for i, j in itertools.product(range(3), repeat=2):
    checker = set()
    for a, b in itertools.product(range(3), repeat=2):
        checker.add(grid[i*3 + a][j*3 + b])
    if len(checker) != 9:
        print("No")
        exit()

print("Yes")