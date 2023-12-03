import sys
import io
import math, bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
7
0 240 720 1320 1440 1800 2160
3
480 1920
720 1200
0 2160
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
As = list(map(int, readline().split()))
cumsum = [0]
for i in range((N-1) // 2):
    a, b = As[i*2], As[i*2+1]
    cumsum.append(cumsum[-1] + b - a)
Q = int(input())
for i in range(Q):
    l, r = map(int, readline().split())
    il = bisect.bisect_right(As, l)
    ir = bisect.bisect_right(As, r)
    if il % 2 == 0:
        minus = cumsum[il // 2]
    else:
        minus = cumsum[(il - 1) // 2] + l - As[il-1]
    
    if ir % 2 == 0:
        plus = cumsum[ir // 2]
    else:
        plus = cumsum[(ir - 1) // 2] + r - As[ir - 1]
    print(r - l - plus + minus)