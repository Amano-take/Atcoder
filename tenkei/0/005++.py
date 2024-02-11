import sys
import io
import math
sys.setrecursionlimit(10**8)

_INPUT = """\
1000000000000000000 29 6
1 2 4 5 7 9
"""
sys.stdin = io.StringIO(_INPUT)

#dfs

ANSDIV = 10**9 + 7

#logNで終わらせる

def mul(dpi, dpj, tj):
    res = [0] * B
    for p in range(B):
        for q in range(B):
            res[(p*tj + q) % B] += dpi[p] * dpj[q]
            res[(p*tj + q) % B] %= ANSDIV
    return res

N, B, K = map(int, input().split())
C = list(map(lambda x: int(x) % B, input().split()))

#桁数
LOG = int(math.log(N, 2)) + 1
ten = [10] * LOG
for i in range(1, LOG):
    ten[i] = (ten[i-1] * ten[i-1]) % B

dubling = [[0] * B for _ in range(LOG)]

for c in C:
    dubling[0][c] += 1

for i in range(1, LOG):
    dubling[i] = mul(dubling[i-1], dubling[i-1], ten[i-1])

res = [0] * B
res[0] = 1
for i in range(LOG):
    if N & (1 << i):
        res = mul(res, dubling[i], ten[i])

print(res[0])