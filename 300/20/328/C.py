import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 1
aaaaa
1 5
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()

N, Q = map(int, readline().split())
S = readline()
bef = [0]
for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        bef.append(1)
    else:
        bef.append(0)

for i in range(len(bef)-1):
    bef[i+1] += bef[i]

for j in range(Q):
    l, r = map(int, readline().split())
    print(bef[r-1] - bef[l-1])