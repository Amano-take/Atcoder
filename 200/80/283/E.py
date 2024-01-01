import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 4
1 0 0 0
0 1 1 1
0 0 1 0
1 1 0 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
isolated = [[True]*W for _ in range(H)]
for j, row in enumerate(grid):
    for i in range(H-1):
        if row[i] == row[i+1]:
            isolated[j][i] = False
            isolated[j][i+1] = False
ans = []
finalreverse = None
previous_reverse_flag = False
temp = 0
for i in range(1, H):
    reverse_flag = None
    for j in range(W):
        if reverse_flag is None and isolated[i-1][j] == True:
            reverse_flag = (grid[i][j] ^ grid[i-1][j])^previous_reverse_flag
        elif isolated[i-1][j] == True:
            if reverse_flag != (grid[i][j] ^ grid[i-1][j]) ^ previous_reverse_flag:
                print(-1)
                exit()
    if reverse_flag is None:
        ans.append((temp, i))
        reverse_flag = False
        temp = 0
    elif reverse_flag:
        temp += 1
    for j in range(W):
        if isolated[i][j] == True and grid[i-1][j] ^ previous_reverse_flag == grid[i][j] ^ reverse_flag:
            isolated[i][j] = False
    
    if i == H-1:
        finalreverse = reverse_flag
        ans.append((temp, i + 1))
    else:
        previous_reverse_flag = reverse_flag
for j in range(W):
    if isolated[-1][j] == True:
        if finalreverse != grid[-1][j] ^ grid[-2][j]:
            print(-1)
            exit()
total = 0
start = 0
for num, end in ans:
    total += min(num, end - start - num)
    start = end
print(total)