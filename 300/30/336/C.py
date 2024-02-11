import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
31415926535
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()


N = int(input())
N -= 1
ans = []
while True:
    ans.append(N%5)
    N //= 5
    if N == 0:
        break
ans.reverse()
cand = [0, 2, 4, 6, 8]
ansstr = ""
for i in ans:
    ansstr += str(cand[i])
print(ansstr)

