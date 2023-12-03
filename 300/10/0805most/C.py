import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
10
999999997 999999999 4 3 2 4 999999990 8 999999991 999999993
"""
sys.stdin = io.StringIO(_INPUT)
 
N = int(input())
l = list(map(int, input().split()))
sum = sum(l)
target = sum // N
plus = sum - target * N
minus = N - plus
ans = 0
for v in l:
    if v > target and plus > 0:
        ans += v - (target + 1)
        plus -= 1
    elif v > target:
        ans += v - target
    elif v < target and minus > 0:
        ans += target - v
        minus -= 1
    elif v < target:
        ans += target + 1 - v
print(ans // 2)