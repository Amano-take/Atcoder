import sys
import io
import math

sys.setrecursionlimit(10**8)
_INPUT = """\
atcoder
"""
sys.stdin = io.StringIO(_INPUT)

L = {"a", "e", "i", "o", "u"}

S = input()
ans = ""
for s in S:
    if s not in L:
        ans += s
print(ans)