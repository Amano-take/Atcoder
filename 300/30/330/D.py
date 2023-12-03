import sys
import io
import math
import itertools
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
15
xooxxooooxxxoox
oxxoxoxxxoxoxxo
oxxoxoxxxoxoxxx
ooooxooooxxoxxx
oxxoxoxxxoxoxxx
oxxoxoxxxoxoxxo
oxxoxooooxxxoox
xxxxxxxxxxxxxxx
xooxxxooxxxooox
oxxoxoxxoxoxxxo
xxxoxxxxoxoxxoo
xooxxxooxxoxoxo
xxxoxxxxoxooxxo
oxxoxoxxoxoxxxo
xooxxxooxxxooox
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N = int(input())
board = [list(readline()) for _ in range(N)]
yoko = []
for i in range(N):
    yoko.append(board[i].count("o"))
tate = []
for i in range(N):
    t = 0
    for j in range(N):
        if board[j][i] == "o":
            t += 1
    tate.append(t)
ans = 0
for (i, j) in itertools.product(range(N), repeat=2):
    if board[i][j] == "o":
        ans += (tate[j] - 1) * (yoko[i] - 1)
print(ans)