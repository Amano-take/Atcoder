import sys
import io
import math
import heapq
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 5
2 0
5 2
0 3
3 2
3 4
1 5
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, K = map(int, readline().split())
Xs, Ys= map(list, zip(*[list(map(int, readline().split())) for _ in range(N)]))
Xs.sort()
Ys.sort()
difX = Xs[-1] - Xs[0]
difY = Ys[-1] - Ys[0]
while True:
    if difX > difY:
        