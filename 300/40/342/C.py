import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
7
atcoder
4
r a
t e
d v
a r
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
S = input()
dic = ddict(str)
for i in range(26):
    dic[chr(i+97)] = chr(i+97)

for i in range(int(input())):
    a, b = input().split()
    for i in range(26):
        if dic[chr(i+97)] == a:
            dic[chr(i+97)] = b



ans = []
for s in S:
    ans.append(dic[s])
print("".join(ans))
