import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
3
3 2 4
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
A = map(int, readline().split())
lA = list(A)
a = lA[0]
for at in lA:
    if a != at:
        print("No")
        break
else:
    print("Yes")