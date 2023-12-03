import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
53
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
c1 = (N // 5 ) * 5
if N % 5 >= 3:
    print(c1 + 5)
else:
    print(c1)