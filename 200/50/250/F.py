import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import time
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4
4 4
-4 4
-4 -4
4 -4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]


    S_double = 0
    for i in range(1, N-1):
        S_double += (XY[i][0] - XY[0][0]) * (XY[i+1][1] - XY[0][1]) - (XY[i][1] - XY[0][1]) * (XY[i+1][0] - XY[0][0])

    left = 0
    right = 2
    s = (XY[1][0] - XY[0][0]) * (XY[2][1] - XY[0][1]) - (XY[1][1] - XY[0][1]) * (XY[2][0] - XY[0][0])
    ans = abs(S_double - s * 4)
    #尺取り法
    while left < N:

        if s * 4 <  S_double:
            nright = (right + 1) % N
            s += (XY[right][0] - XY[left][0]) * (XY[nright][1] - XY[left][1]) - (XY[right][1] - XY[left][1]) * (XY[nright][0] - XY[left][0])
            right = nright
        else:
            nleft = left + 1
            if nleft == N:
                break
            s -= (XY[nleft][0] - XY[left][0]) * (XY[right][1] - XY[left][1]) - (XY[nleft][1] - XY[left][1]) * (XY[right][0] - XY[left][0])
            left = nleft
        ans = min(ans, abs(S_double - s * 4))
    print(ans)
solve()