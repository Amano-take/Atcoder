import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1000000000 1000000000000 998244353
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
A, X, M = map(int, input().split())
#ans is A^0 + A^1 + A^2 + ... + A^X-1 mod M
#(A^0 + A^1 + ... + A^(X-1)) * (A - 1) = A^X - 1
#(A^0 + A^1 + ... + A^(X-1)) = (A^X - 1) / (A - 1)

if A == 1:
    print(X % M)
    exit()


ans = pow(A, X, M) - 1
div = pow(A-1, -1, M)
print(ans * div % M)

for i in range(1, 16):
    div = pow(i, -1, 16)
    print(div, div*i % 16)