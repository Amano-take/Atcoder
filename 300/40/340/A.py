import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

input=lambda: sys.stdin.readline().strip()
A, B, D = map(int, input().split())
ans = []
temp = A
while True:
    ans.append(temp)
    temp += D
    if temp > B:
        break
print(*ans)