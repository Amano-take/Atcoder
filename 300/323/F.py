import sys
import io
import math
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT = """\
5 7
1 2 3 6
1 2 0 5
2 3 1 5
2 4 5 3
2 5 1 9
3 4 4 8
4 5 2 7
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
graph = ddict(list)
mask = (1 << 20) - 1
for _ in range(M):
    u1, v1, b1, c1 = map(int, readline().split())
    key = (u1 << 20) + v1
    value = (b1 << 20) + c1
    graph[key].append(value)
graph = dict(sorted(graph.items(), key=lambda x: x[0]&mask))


def correct_k(k):
    dp = [-math.inf] * N
    dp[0] = 0
    for key, value in graph.items():
        s = ((key >> 20) & mask) - 1
        e = (key & mask) - 1
        for lv in value:
            b = (lv >> 20) & mask
            c = lv & mask
            if dp[s] != -math.inf:
                dp[e] = max(dp[e], dp[s] + (b - c*k))
    return dp[N-1] >= 0

l = 0
r = 1 << 40
while r - l > 10**(-12):
    if l != 0:
        if (r-l)/l <= 10**(-12):
            break
    if correct_k((l+r)/2):
        l = (l+r)/2
    else:
        r = (l+r)/2
print(l)
