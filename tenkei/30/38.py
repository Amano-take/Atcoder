import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
A, B = map(int, input().split())

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extgcd(b, a % b)
        return d, y, x - y * (a // b)

g, _, _ = extgcd(A, B)
gcd = A // g * B
if gcd > 10**18:
    print("Large")
else:
    print(gcd)

