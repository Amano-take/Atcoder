import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
1 2 6 4 5
2 3 1 5 4
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_dic = ddict(lambda: inf)
for i, b in enumerate(B):
    if B_dic[b] == inf:
        B_dic[b] = i

A_list = []
for a in A:
    A_list.append(B_dic[a])

maxA = [A_list[0]]
for a in A_list[1:]:
    maxA.append(max(maxA[-1], a))

A_dic = ddict(lambda: inf)
for i, a in enumerate(A):
    if A_dic[a] == inf:
        A_dic[a] = i

B_list = []
for b in B:
    B_list.append(A_dic[b])

maxB = [B_list[0]]
for b in B_list[1:]:
    maxB.append(max(maxB[-1], b))



Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    index = maxA[l-1]
    if maxA[l-1] <= r -1 and maxB[r-1] <= l-1:
        print("Yes")
    else:
        print("No")
