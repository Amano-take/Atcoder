import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
1 4 1 4 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
sortA = sorted(As)
cumsum = [0]
for a in sortA:
    cumsum.append(cumsum[-1] + a)

for i in As:
    index = bisect.bisect_right(sortA, i)
    print(cumsum[-1] - cumsum[index])