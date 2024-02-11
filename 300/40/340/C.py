import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
190
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())

mem = ddict(lambda: inf)
mem[0] = 0
mem[1] = 0
mem[2] = 2
def f(x):
    if mem[x] != inf:
        return mem[x]
    if x % 2 == 0:
        t = x // 2
        mem[x] =  x + f(t)*2
    else:
        t = (x-1) // 2
        mem[x] = f(t) + f(t+1) + x
    return mem[x]
print(f(N))
