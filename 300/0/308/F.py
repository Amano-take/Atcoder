import sys
import io
import bisect
import math
from sortedcontainers import SortedList
sys.setrecursionlimit(10**8)
_INPUT = """\
10 5
9 7 1 5 2 2 5 5 7 6
7 2 7 8 2
3 2 4 1 2
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
Ps = list(map(int, readline().split()))
Ls = list(map(lambda x: -int(x), readline().split()))
Ds = list(map(int, readline().split()))
LDs = list(zip(Ds, Ls))
sl = SortedList(Ps)
LDs.sort(reverse=True)
ans = sum(Ps)
for l, d in LDs:
    d = -d
    index = sl.bisect_left(d)
    if index == len(sl):
        continue
    else:
        sl.pop(index)
        ans -= l
print(ans)