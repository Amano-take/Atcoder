import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
2 3 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, M, K = map(int, input().split())

l = 0
r = max(N, M) * K
g = math.gcd(N, M)
g = N * M // g

def check(x):
    return (x // N) + (x // M) - (x // g)*2 >= K

while r - l > 1:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)