import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
10 2
1 2 3 4 4 3 2 1 2 3
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
As = list(map(int, input().split()))
#尺取り法
right = 0
left = 0
d = ddict(int)
ans = 0
while right < N:
    d[As[right]] += 1
    if len(d) <= K:
        ans = max(ans, right - left + 1)
    while len(d) > K:
        d[As[left]] -= 1
        if d[As[left]] == 0:
            del d[As[left]]
        left += 1
    right += 1
print(ans)