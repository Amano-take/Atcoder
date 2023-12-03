import sys
import io
import math
import bisect
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT = """\
7 6
5
6 1
3 1
4 2
1 5
6 2
2
2 5
2
3 4
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
W, H = map(int, readline().split())
N = int(input())
pq = [tuple(map(int, readline().split())) for _ in range(N)]
pq.sort()
Ys = []
start = 0
A = int(input())
As = list(map(int, readline().split()))
for a in As:
    i = bisect.bisect_left(pq, (a, 0))
    Ys.append(pq[start:i])
    start = i
else:
    Ys.append(pq[start:])
B = int(input())
Bs = list(map(int, readline().split()))
Bs.append(H)
ansmin = N+1
ansmax = -1
for y in Ys:
    index = ddict(int)
    for yy in y:
        i = bisect.bisect_left(Bs, yy[1])
        index[i] += 1
    if len(index) != B+1:
        ansmin = 0
    elif ansmin != 0:
        ansmin = min(ansmin, min(index.values()))

    if len(index) != 0:
        ansmax = max(ansmax, max(index.values()))
        
print(ansmin)
print(ansmax)