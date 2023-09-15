
import sys
import io
from collections import defaultdict

sys.setrecursionlimit(10**8)
_INPUT = """\
3
1 2
3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
edge = defaultdict(int)
for i in range(N-1):
    Dlist = list(map(int, readline().split()))
    for e, d in enumerate(Dlist):
        end = i+e+1
        edge[(i, end)] = d
        edge[(end, i)] = d

pair = defaultdict(int)
for i in range(N-1):
    for j in range(i+1, N):
        pair[(i, j)] = (1<<i) + (1 << j)


dp = [[0] * (1<<N) for _ in range(N//2 + 1)]
pairitem = pair.items()
for i in range(N//2):
    for j in range(1<<N):
        rest = (1<<N) - 1 - j
        for pa, value in pairitem:

            if value == (value & rest):
                dp[i+1][j | value] = max(dp[i+1][j | value], dp[i][j] + edge[pa])
print(dp[-1][-1])
