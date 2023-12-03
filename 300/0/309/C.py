import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
4 100
6 3
2 5
1 9
4 2
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, K = map(int, readline().split())
medic = []
for _ in range(N):
    a, b = map(int, readline().split())
    medic.append((a, b))

medic.sort(reverse=True)
sum = 0
for a, b in medic:
    sum += b
    if sum > K:
        print(a+1)
        break
else:
    print(1)
