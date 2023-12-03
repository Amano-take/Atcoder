import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
13 3
9 5 2 7 1 8 8 2 1 5 2 3 100
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))
mojisu = sum(L) + len(L) - M
if mojisu % M == 0:
    saitei = mojisu // M
else:
    saitei = mojisu // M + 1

saitei = max(saitei, max(L))

def count(W, L):
    c = 1
    moji = 0
    for l in L:
        if moji == 0:
            moji += l
        elif moji + l + 1 <= W:
            moji += l+1
        else:
            c += 1
            moji = l
    return c

l = saitei - 1
r = sum(L) + len(L)
while r - l != 1:
    mid = (r+l) // 2
    if count(mid, L) <= M:
        r = mid
    else:
        l = mid
print(r)
