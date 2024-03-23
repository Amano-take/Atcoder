import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
99999 1000000000000000000
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
def dig_sum(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res

cycle = [-1] * (10 ** 5)
cycle[N] = 0
while True:
    n = N + dig_sum(N)
    n %= 10 ** 5
    if cycle[n] != -1:
        break
    cycle[n] = cycle[N] + 1
    if cycle[n] == K:
        print(n)
        exit()
    N = n

cycle_len = cycle[N] - cycle[n] + 1
cycle_K = (K - cycle[n]) % cycle_len

start = n
for _ in range(cycle_K):
    start += dig_sum(start)
    start %= 10 ** 5
print(start)