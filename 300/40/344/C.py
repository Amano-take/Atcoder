import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
1 2 3
2
2 4
6
1 2 4 8 16 32
4
1 5 10 50
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))

s = set()
for a in A:
    for b in B:
        for c in C:
            s.add(a+b+c)

q = int(input())
Q = list(map(int, input().split()))
for q in Q:
    if q in s:
        print("Yes")
    else:
        print("No")