import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
Ns = map(int, readline().split())
ans = 0
for i, n in enumerate(Ns):
    ans += n << i

print(ans)