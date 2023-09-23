import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
9 9
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

A, B = map(int, readline().split())
print(int(math.pow(A, B) + math.pow(B, A)))