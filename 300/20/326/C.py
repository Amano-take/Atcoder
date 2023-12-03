import sys
import io
import math
from collections import deque

sys.setrecursionlimit(10**8)
_INPUT = """\
10 1
3 1 4 1 5 9 2 6 5 3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, readline().split())
present = list(map(int, readline().split()))
present.sort()
ans = 0
pre = deque()
for p in present:
    while len(pre) != 0:
        st = pre[0]
        if st + M <= p:
            pre.popleft()
        else:
            break
    pre.append(p)
    ans = max(ans, len(pre))

print(ans)
