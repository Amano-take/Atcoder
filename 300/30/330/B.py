import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 4 7
3 1 4 9 7
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, L, R = map(int, readline().split())
As = list(map(int, readline().split()))
for i in range(N):
    a = As[i]
    if L <= a <= R:
        print(a)
    else:
        if a < L:
            print(L)
        else:
            print(R)