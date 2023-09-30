import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
10
822981260158260522 52 20
760713016476190629 2314654 57
1312150450968417 1132551176249851 7
1000000000000000000 1083770654 79
234122432773361868 170290518806790 23
536187734191890310 61862 14
594688604155374934 53288633578 39
1000000000000000000 120160810 78
89013034180999835 14853481725739 94
463213054346948152 825589 73
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
for _ in range(N):
    M, X, K = map(int, readline().split())
    ans = 0
    root = X
    removal = X
    while root != 0 and K >= 0:
        if K == 0:
            ans += 1
            break
        if root == X:
            sa = root * (2 ** K)
            sb = (root+1) * (2 ** K) - 1
            if sa <= M:
                ans += min(M, sb) - sa + 1
            removal = root
            root = root // 2
            K -= 1
        else:
            sa = root * (2 ** K)
            sb = (root+1) * (2 ** K) - 1
            rsa = removal * (2 ** (K - 1))
            rsb = (removal + 1) * (2 ** (K -1)) - 1
            if sa <= M:
                if rsa <= M:
                    ans += min(M, sb) - sa + 1 - ( min(M, rsb) - rsa + 1)
            removal = root
            root = root // 2
            K -= 1
    print(ans)