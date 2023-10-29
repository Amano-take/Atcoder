import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
1001000000001010
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S = list(input())
N = len(S)
for i in range(1, N, 2):
    if S[i] != "0":
        print("No")
        break
else:
    print("Yes")