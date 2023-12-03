import sys, io
import math, heapq
from collections import defaultdict as ddict, deque
from itertools import product, permutations, combinations

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
15
10
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
H1, H2 = map(int, readline().split())
print(H1 - H2)