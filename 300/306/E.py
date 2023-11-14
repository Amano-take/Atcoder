import sys
import io
import math
from sortedcontainers import SortedList

sys.setrecursionlimit(10**8)
_INPUT = """\
4 2 10
1 5
2 1
3 3
4 2
2 10
1 0
4 0
3 1
2 0
3 0
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, K, Q = map(int, readline().split())
As = [0] * N
sl = SortedList(As)
ans = 0
for _ in range(Q):
    index, value = map(int, readline().split())
    old = As[index-1]
    As[index-1] = value
    if sl.bisect_left(old) > N - K -1:
        ans -= old
        sl.remove(old)
        if sl.bisect_left(value) >= N - K:
            ans += value
            sl.add(value)
        else:
            ans += sl[N - K -1]
            sl.add(value)
    else:
        if sl.bisect_left(value) > N - K:
            ans -= sl[N - K]
            ans += value
            sl.remove(old)
            sl.add(value)
        else:
            sl.remove(old)
            sl.add(value)
    print(ans)


