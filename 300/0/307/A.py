import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
2
1000 2000 3000 4000 5000 6000 7000 2000 3000 4000 5000 6000 7000 8000
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
ans = []
ho = list(map(int, readline().split()))
for i in range(N):
    t = 0
    for j in range(7):
        t += ho[i*7 + j]
    ans.append(t)
print(*ans)