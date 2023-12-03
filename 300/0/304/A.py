import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
20230603
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S = list(input())
ans = []
for i in range(len(S)):
    if i < 3:
        ans.append(S[i])
    else:
        ans.append("0")
print("".join(ans))