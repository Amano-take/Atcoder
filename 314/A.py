import sys
import io
import math
sys.setrecursionlimit(10**8)

_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
N+=1
s = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

for i, st in enumerate(s):
    if i == N+1:
        break
    print(st, end="")

