import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N = int(input())
for i in range(1, 20):
    if N == pow(i, i):
        print(i)
        exit()
print(-1)