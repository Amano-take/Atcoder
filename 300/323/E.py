import sys
import io
import math
import bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
10 ms
mkgn
m
hlms
vmsle
mxsm
nnzdhi
umsavxlb
ffnsybomr
yvmm
naouel
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, T = input().split()
N = int(N)
lenT = len(T)
ls = []
rs = []
for i in range(N):
    S = readline().strip()
    i = 0
    for s in S:
        if i == len(T):
            break
        if s == T[i]:
            i += 1
    ls.append(i)
    i = len(T)-1
    for s in S[len(S)::-1]:
        if i == -1:
            break
        if s == T[i]:
            i -= 1
    rs.append(i)
lenrs = len(rs)
rs.sort()
ans = 0
for i in ls:
    t = bisect.bisect_right(rs, i - 1)
    ans += t
print(ans)