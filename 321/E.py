import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
5
10 2 0
10 2 1
10 2 2
10 2 3
10 2 4
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
for _ in range(N):
    M, X, K = map(int, readline().split())
    ans = 0
    root = X
    while root != 0:
        sa = root * (2 ** K)
        sb = (root+1) * (2 ** K) - 1
        if sa <= M:
            ans += min(M, sb) - sa + 1