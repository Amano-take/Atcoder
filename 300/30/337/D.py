import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4 3
xo.x
..o.
xx.o
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

H, W, K = map(int, input().split())
def simpleline(s):
    if len(s) < K:
        return 2 * 10**6
    ans = 0
    for i in range(K):
        if s[i] == "x":
            ans += 2*10**6
        if s[i] == ".":
            ans += 1
    res = ans
    for i in range(K, len(s)):
        if s[i] == "x":
            ans += 2*10**6
        if s[i - K] == "x":
            ans -= 2*10**6
        if s[i] == ".":
            ans += 1
        if s[i - K] == ".":
            ans -= 1
        res = min(res, ans)
    return res

grid = [list(input()) for _ in range(H)]
ans = inf
for h in range(H):
    ans = min(ans, simpleline(grid[h]))
for w in range(W):
    ans = min(ans, simpleline([grid[h][w] for h in range(H)]))
if ans > K:
    print(-1)
else:
    print(ans)