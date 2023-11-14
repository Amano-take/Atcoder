from collections import deque
import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
5
a(b)(
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

parentheses = deque()
N = int(input())
S = list(input())
imos = [0] * (N+1)

for i, s in enumerate(S):
    if s == "(":
        parentheses.append(i)
    elif s == ")":
        if len(parentheses) != 0:
            start = parentheses.pop()
            end = i
            imos[start] += 1
            imos[end + 1] -= 1

for i in range(N):
    imos[i+1] += imos[i]

ans = []
for i in range(N):
    if imos[i] == 0:
        ans.append(S[i])
    
print("".join(ans))
    