import sys
import io
sys.setrecursionlimit(10**8)
_INPUT="""\
4 3 2
"""
sys.stdin=io.StringIO(_INPUT)
a, b, c = map(int, input().split())

if a < c**b:
    print("Yes")
else:
    print("No")