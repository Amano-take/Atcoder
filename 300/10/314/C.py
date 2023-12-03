import sys
import io
from collections import deque
sys.setrecursionlimit(10**8)
_INPUT="""\
8 3
apzbqrcs
1 2 3 1 2 2 1 2
"""
sys.stdin=io.StringIO(_INPUT)

N, M = map(int, input().split())
S = input()
Clist = list(map(int, input().split()))
color = [deque() for _ in range(M)]
flag = [ False] * M

for i, c in enumerate(Clist):
    color[c-1].append(S[i])

ans=["a"] * N
for i, c in enumerate(Clist):
    if not flag[c-1]:
        ans[i] = color[c-1].pop()
        flag[c-1] = True
    else:
        ans[i] = color[c-1].popleft()
print("".join(ans))