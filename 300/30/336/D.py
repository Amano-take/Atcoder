import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10
1 2 3 1 10 10 10 10 10 10 
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))

now = 1
right = [0] * N
for i, a in enumerate(As):
    if a >= now:
        right[i] = now
        now += 1
    else:
        now = a
        right[i] = now
        now += 1

print(right)
reversedA = As[::-1]
now = 1
left = [0] * N
for i, a in enumerate(reversedA):
    if a >= now:
        left[i] = now
        now += 1
    else:
        now = a
        left[i] = now
        now += 1
left = left[::-1]
ans = 0

for i in range(N):
    ans = max(ans, min(left[i], right[i]))
print(ans)