import sys
import io
import math
from collections import defaultdict as ddict
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1
x
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N = int(input())
S = readline() + "1"
before = "1"
C = ddict(int)
c = 0
for s in S:
    if s == before:
        c += 1
    else:
        C[before] = max(C[before], c)
        c = 1
    before = s

print(sum(C.values()))