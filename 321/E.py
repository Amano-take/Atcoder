import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
5
10 2 0
10 2 1
10 2 2
10 2 3
10 4 3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
for _ in range(N):
    M, X, K = map(int, readline().split())
    if K > M.bit_length() << 1:
        print(0)
        continue
    ans = 0
    root = X
    removal = X
    while root != 0 and K >= 0:
        if K == 0:
            ans += 1
            break
        if root == X:
            sa = root << K
            sb = ((root+1) << K) - 1
            if sa <= M:
                ans += min(M, sb) - sa + 1
            removal = root
            root >>= 1
            K -= 1
        else:
            sa = root << K
            sb = ((root+1) << K) - 1
            rsa = removal << (K-1)
            rsb = ((removal + 1) << (K-1) )- 1
            if sa <= M:
                if rsa <= M:
                    ans += min(M, sb) - sa + 1 - ( min(M, rsb) - rsa + 1)
                else:
                    ans += min(M, sb) - sa + 1
            removal = root
            root >>= 1
            K -= 1
    print(ans)