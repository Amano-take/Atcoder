import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
2 5 7 8
5
2 9 10 11 19
20
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

cantgo = set(B)
reachable = [False] * (X+1)
reachable[0] = True
for i in range(0, X+1):
    if reachable[i] == True:
        for a in A:
            if i + a <= X and i + a not in cantgo:
                reachable[i+a] = True
    
if reachable[X] == True:
    print("Yes")
else:
    print("No")