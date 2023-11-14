import sys
import io
import math

from sortedcontainers import SortedList
sys.setrecursionlimit(10**8)
_INPUT = """\
3 2
1 3
2 8
4 6
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())


#slじゃなくてBITでもいけるな
As = [sorted(map(int, readline().split())) for _ in range(N)]
sl = SortedList(As[-1])
rank = []
for i in range(N-2, -1, -1):
    temp = []
    for a in As[i]:
        temp.append(sl.bisect_right(a))
        sl.add(a)
    rank.append(temp)

ans = 0
for i, r in enumerate(rank):
    ans += i * M * (M - 1) // 2 + sum(r) + (i+1) * M
print(ans)