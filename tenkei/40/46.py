import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict, Counter
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
10 13 93
5 27 35
55 28 52
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

def divide46(x):
    return int(x) % 46

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
countA = Counter(map(divide46, A))
countB = Counter(map(divide46, B))
countC = Counter(map(divide46, C))
ans = 0
for i in countB:
    for j in countC:
        k = (46 - i - j) % 46
        if k in countA:
            ans += countA[k] * countB[i] * countC[j]
print(ans)
        
