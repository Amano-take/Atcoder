import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 60
60 20 100 90 40
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, L = map(int, readline().split())
As = list(map(int, readline().split()))
ans = 0
for a in As:
    if a >= L:
        ans += 1
print(ans)