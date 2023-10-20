import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
324
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
while N != 1:
    if N % 3 == 0:
        N = N // 3
    elif N % 2 == 0:
        N = N // 2
    else:
        print("No")
        exit()
print("Yes")