import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 1 2
2 3 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, L, R = map(int, input().split())
As = list(map(int, input().split()))
maxA = max(As)
i, j = 0, 0
bitree = [(i, j)]
while True:
    if bitree[-1][0] > bitree[-1][1]:
        bitree.append((bitree[-1][0], bitree[-1][1]+1))
    else:
        bitree.append((bitree[-1][0]+1, bitree[-1][1]))

    if bitree[-1][0] * L + bitree[-1][1] * R > maxA:
        break
lotree = [ L * i for i in range(maxA // L + 1)]
bitree = list(map(lambda x: x[0]*L+x[1]*R, bitree))
kati = 1
winner = 1
for a in As:
    print(kati, a)
    if kati == 1:
        index = bisect.bisect_right(bitree, a)
        if index % 2 == 0:
            kati  = -1
        else:
            kati  = 1

    else:
        index = bisect.bisect_right(lotree, a)
        if index % 2 == 0:
            kati  = -1
        else:
            kati  = 1

if kati == 1:
    print("First")
else:
    print("Second")
    