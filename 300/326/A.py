import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
99 96
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
X, Y = map(int, readline().split())
if X > Y:
    if X - Y <= 3:
        print("Yes")
    else:
        print("No")
else:
    if Y - X <= 2:
        print("Yes")
    else:
        print("No")