import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
aaa 10
bbb 20
aaa 30
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
poem_set = set()
ans = 0
ans_score = -1
for i in range(N):
    s, t = input().split()
    t = int(t)
    if s in poem_set:
        continue
    if t > ans_score:
        ans = i
        ans_score = t
    poem_set.add(s)
print(ans+1)
        
