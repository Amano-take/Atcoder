import sys
import io
import math
sys.setrecursionlimit(10**8)
inf = float("inf")
_INPUT = """\
3
3 5 10
4 3 3
2 2 6
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
D = list(map(int, readline().split()))
L1, C1, K1 = map(int, readline().split())
L2, C2, K2 = map(int, readline().split())
dp = [inf] * (max(D) + 1)
dp[0] = 0
for i in range(1, len(dp)):
    p = i - 