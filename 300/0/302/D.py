import sys
import io
import math, bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
3 3 0
1 3 3
6 2 7
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M, D = map(int, readline().split())
As = list(map(int, readline().split()))
Bs = list(map(int, readline().split()))
Bs.sort()
ans = -1
for a in As:
    index = bisect.bisect_right(Bs, a + D)
    if index == 0:
        continue
    else:
        b = Bs[index - 1]
        if b < a - D:
            continue
        else:
            ans = max(ans, a + b)
print(ans)