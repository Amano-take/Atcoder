from collections import deque
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
AAABCABCABCAABCABCBBBAABCBCCCAAABCBCBCC
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
S = readline()
ans = deque()
for i, s in enumerate(S):
    if s == "C":
        if len(ans) >= 2:
            s2 = ans[-1]
            s1 = ans[-2]
            if s1 == "A" and s2 == "B":
                ans.pop()
                ans.pop()
            else:
                ans.append(s)
        else:
            ans.append(s)
    else:
        ans.append(s)

print("".join(ans))