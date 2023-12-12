import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8 3 4
1 4
2 1
3 3
1 2
3 2
2 3
3 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
L, N1, N2 = map(int, input().split())
As = [list(map(int, input().split())) for _ in range(N1)]
Bs = [list(map(int, input().split())) for _ in range(N2)]
cumsumB = [0] * (N2 + 1)
for i in range(N2):
    cumsumB[i+1] = cumsumB[i] + Bs[i][1]
start = 0
ans = 0

for v, l in As:
    end = start + l
    indexs = bisect.bisect_right(cumsumB, start)
    indexe = bisect.bisect_left(cumsumB, end)
    if indexs == indexe and v == Bs[indexs-1][0]:
        ans += end - start
        start = end
        continue

    if v == Bs[indexs-1][0]:
        ans += cumsumB[indexs] - start
    if v == Bs[indexe-1][0]:
        ans += end - cumsumB[indexe-1]
    for i in range(indexs + 1, indexe):
        if v == Bs[i-1][0]:
            ans += Bs[i-1][1]
    start = end
print(ans)