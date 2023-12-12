import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 6
20 25 30 100
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
As = list(map(int, input().split()))
gcdA = As[0]
for i in range(1, N):
    gcdA = math.gcd(gcdA, As[i])
divA = list(map(lambda x: x//gcdA, As))
divA.sort()
hq = []
heapq.heapify(hq)
for i in range(N):
    heapq.heappush(hq, divA[i])
ans = 0
varset = set()
while len(hq) > 0:
    x = heapq.heappop(hq)
    if x in varset:
        continue
    varset.add(x)
    ans += 1
    if ans == K:
        print(x*gcdA)
        exit()
    else:
        for i in range(N):
            if x + divA[i] not in varset:
                heapq.heappush(hq, x+divA[i])


