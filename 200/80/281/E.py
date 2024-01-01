import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
from sortedcontainers import SortedList
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 1 1
1 2 1 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M, K = map(int, input().split())
As = list(map(int, input().split()))
sc = SortedList()
for i in range(M):
    sc.add(As[i])
ans = 0
for i in range(K):
    ans += sc[i]
anss = []
anss.append(ans)
for i in range(M, N):
    removal = As[i-M]
    addition = As[i]
    if M == K and M == 1:
        anss.append(addition)
        continue
    
    if sc.bisect_right(removal) > K:
        sc.remove(removal)
    else:
        sc.remove(removal)
        ans -= removal
        ans += sc[K-1]
    
    if sc.bisect_left(addition) < K:
        ans += addition
        ans -= sc[K-1]
        sc.add(addition)
    else:
        sc.add(addition)
    anss.append(ans)
print(*anss)