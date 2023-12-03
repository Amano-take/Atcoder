import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
6
3 1 4 1 5 9
"""
sys.stdin = io.StringIO(_INPUT)
M = int(input())
D = list(map(int, input().split()))
sum = sum(D)
mid = (sum + 1) // 2
month = 1
for d in D:
    if mid <= d:
        print(month, mid)
        break
    else:
        mid -= d
        month += 1
