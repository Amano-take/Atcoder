import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
1 1 2
1 2 9
2 1 8
3 2 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
rowscore = ddict(int)
colscore = ddict(int)
notzero = ddict(int)
for i in range(N):
    r, c, x =  map(int, input().split())
    rowscore[r] += x
    colscore[c] += x
    notzero[(r, c)] = x

rowscores = sorted(rowscore.items(), key=lambda x: x[1], reverse=True)
colscores = sorted(colscore.items(), key=lambda x: x[1], reverse=True)

ans = 0
hq = []
heapq.heappush(hq, (-rowscores[0][1] - colscores[0][1], (0, 0)))
while len(hq) > 0:
    score, (r, c) = heapq.heappop(hq)
    score *= -1
    row = rowscores[r][0]
    col = colscores[c][0]
    if score <= ans:
        break
    if (row, col) in notzero:
        ans = max(ans, score - notzero[(row, col)])
    else:
        ans = max(ans, score)

    if r + 1 < len(rowscores):
        heapq.heappush(hq, (-rowscores[r+1][1] - colscores[c][1], (r+1, c)))
    if c + 1 < len(colscores):
        heapq.heappush(hq, (-rowscores[r][1] - colscores[c+1][1], (r, c+1)))

print(ans)