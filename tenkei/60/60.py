import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

_INPUT = """\
10
1 5 6 3 4 5 2 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
A_rev = A[::-1]

def op(x, y):
    ax, ix = x
    ay, iy = y
    if ax > ay:
        return x
    elif ax == ay:
        return x if ix > iy else y
    else:
        return y

def e():
    return (-inf, -1)

def lis(A):
    n = len(A)
    dp = [inf] * n 
    lis_idx = [1] * n
    for i, a in enumerate(A):
        print(dp)
        dp[bisect.bisect_left(dp, a)] = min(dp[bisect.bisect_left(dp, a)], a)
        lis_idx[i] = bisect.bisect_left(dp, inf)
    return lis_idx

lis_idx = lis(A)
lis_idx_rev = lis(A_rev)[::-1]
ans = 0
for i in range(N):
    ans = max(ans, lis_idx[i] + lis_idx_rev[i] - 1)
print(ans)

