import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
144
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
for i in range(100, 920):
    st = list(str(i))
    a, b, c  = map(int, st)
    if i >= N and a*b == c:
        print(i)
        break