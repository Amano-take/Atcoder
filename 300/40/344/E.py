import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

_INPUT = """\
4
2 1 4 3
4
2 1
1 4 5
2 2
1 5 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
A.append(-2)
A.insert(0, -1)

Q = int(input())
dict = ddict(tuple)

for i, a in enumerate(A):
    if i == 0:
        dict[a] = (-1, A[i+1])
        continue
    elif i == N+1:
        dict[a] = (A[i-1], -2)
        continue
    dict[a] = (A[i-1], A[i+1])

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        x, y = q 
        dict[y] = (x, dict[x][1])
        dict[x] = (dict[x][0], y)
        dict[dict[y][1]] = (y, dict[dict[y][1]][1])
    elif t == 2:
        x = q[0]
        alpha = dict[x][0]
        beta = dict[x][1]
        del dict[x]
        dict[alpha] = (dict[alpha][0], beta)
        dict[beta] = (alpha, dict[beta][1])

ans = [-1]
while True:
    ans.append(dict[ans[-1]][1])
    if ans[-1] == -2:
        break
print(*ans[1:-1])
