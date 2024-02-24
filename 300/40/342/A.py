import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
zzzzzzzzzzzzzzzwz
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
S  = input()
if S.count(S[0]) > S.count(S[1]):
    print(S.index(S[1])+1)
elif S.count(S[0]) == S.count(S[1]):
    for i, s in enumerate(S):
        if s != S[0]:
            print(i+1)
            break
else:
    print(S.index(S[0])+1)
