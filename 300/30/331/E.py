import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2 3 3
2 1
10 30 20
1 2
2 1
2 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M, L = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
banned = ddict(set)
for _ in range(L):
    c, d = map(lambda x: int(x) - 1, input().split())
    banned[c].add(d)

ans = 0
sortA = sorted(enumerate(As), key=lambda x: x[1], reverse=True)
sortB = sorted(enumerate(Bs), key = lambda x: x[1], reverse=True)
for ia, a in sortA:
    if ans > As[ia] + sortB[0][1]:
        break
    for ib, b in sortB:
        if ans > As[ia] + b:
            break
        if ib not in banned[ia]:
            ans = max(ans, As[ia] + Bs[ib])

print(ans)