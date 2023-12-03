import bisect
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
2 1 3 3 2
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, readline().split()))
As.sort()
print(As[bisect.bisect_left(As, As[-1]) -1])