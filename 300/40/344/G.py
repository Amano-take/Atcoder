import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
atcoder|beginner|contest
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

S = input()
answer = []
flag = False
for s in S:
    if s == "|":
        flag = ~flag
    if not flag and s != "|":
        answer.append(s)

print("".join(answer))