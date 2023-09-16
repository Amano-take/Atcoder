import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
10000 27 7
1 3 4 6 7 8 9
"""
sys.stdin = io.StringIO(_INPUT)

#dfs

ANSDIV = 10**9 + 7

N, B, K = map(int, input().split())
c = list(map(int, input().split()))
ans = 0

def dfs(remain, lc, digit):
    global ans
    if digit == 0:
        if remain == 0:
            ans = (ans + 1) % ANSDIV
        return
    for c in lc:
        r = (c * (10 ** (digit - 1))) % B
        dfs((remain + r) % B, lc, digit-1)

dfs(0, c, N)
print(ans)