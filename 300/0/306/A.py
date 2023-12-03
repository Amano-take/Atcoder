import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
8
beginner
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
ans = []
N = int(input())
S = list(input())
for s in S:
    ans.append(s)
    ans.append(s)
print("".join(ans))