import sys
import io
import math
import time
sys.setrecursionlimit(10**8)
DIV =  998244353
def mat_mul(a, b) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= DIV
    return c


def mat_pow(x, n):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1

    return y

_INPUT = """\
1000000007 28
bbabba
bbbbaa
aabbab
bbbaba
baaabb
babaab
bbaaba
aabaaa
aaaaaa
aabbaa
bbaaaa
bbaabb
bbabab
aababa
baaaba
ababab
abbaba
aabaab
ababaa
abbbba
baabaa
aabbbb
abbbab
baaaab
baabbb
ababbb
baabba
abaaaa
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
banned = set()
for i in range(M):
    s = list(readline().strip())
    s.insert(0, "b")
    v = map(lambda x: str(ord(x) - ord("a")), s)
    v = "".join(v)
    banned.add(v[1:])

if N <= 5:
    ans = 0
    for i in range(1 << N, 1 << (N+1)):
        moji = bin(i)[3:]
        for b in banned:
            if moji.find(b) != -1:
                break
        else:
            ans += 1
    print(ans)
else:
    check = [0] * ( 1 << 6)
    start = [0] * ( 1<< 5)
    for i in range(1 << 6, 1 << 7):
        moji = bin(i)[3:]
        for b in banned:
            if moji.find(b) != -1:
                break
        else:
            index = i & ((1 << 5) - 1)
            start[index] += 1
            check[i - (1 << 6)] = 1

    C = [[0] * (1 << 5) for _ in range(1 << 5)]
    for i in range(1 << 5):
        if check[i << 1]:
            C[i][(i << 1) & ((1 << 5) - 1)] = 1
        if check[(i << 1) + 1]:
            C[i][((i << 1) + 1) & (( 1<<5) - 1)] = 1
    pC = mat_pow(C, N-6)
    print(sum(mat_mul([start], pC)[0]) % DIV)
