import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

input=lambda: sys.stdin.readline().strip()
N = int(input())
M = N.bit_length()
drink = [[] for _ in range(M)]
for i in range(N):
    t = i
    for j in range(M):
        if t % 2 == 1:
            drink[j].append(i+1)
        t //= 2
print(M)
for i in range(M):
    print(len(drink[i]), *drink[i])

sys.stdout.flush()
s = input()
ans =1
for i in range(len(s)):

    if s[i] == "1":
        ans += 2 ** i

print(ans)
    