import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
264428617
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
D = int(input())
x = 0
ans = inf
while True:
    if x ** 2 > D:
        break
    rest = D - x ** 2
    y = int(rest ** (1/ 2))
    ans = min(ans, rest - y ** 2)
    ans = min(ans, (y+1)**2 - rest)
    x += 1
print(ans)