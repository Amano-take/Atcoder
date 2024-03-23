import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, combinations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for bits in range(1, 1 << H):
    rows = []
    for i in range(H):
        if bits >> i & 1:
            rows.append(i)
    dic = ddict(int)
    for w in range(W):
        s = set()
        for r in rows:
            s.add(grid[r][w])
        if len(s) == 1:
            dic[list(s)[0]] += 1
    ans = max(ans, max(dic.values()) * len(rows))
print(ans)

