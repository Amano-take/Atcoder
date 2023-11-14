import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 200
100 675 201 200 199 328
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()

N, X = map(int, readline().split())
Ss = list(map(int, readline().split()))
ans = 0
for s in Ss:
    if s <= X:
        ans += s
print(ans)