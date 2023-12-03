import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
7 8
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
A, B = map(int, readline().split())
if abs(A - B) == 1 and A % 3 != 0:
    print("Yes")
else:
    print("No")