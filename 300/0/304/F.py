import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
510510
##.#.#
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N = int(input())
yakusuu = set()
for i in range(1, int(N**(1/2))+ 1):
    if N % i == 0:
        yakusuu.add(i)
        yakusuu.add(N//i)
print(len(yakusuu))

