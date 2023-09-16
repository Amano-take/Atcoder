import math
import sys
import io
sys.setrecursionlimit(10**8)

def logpow(a, b, ANSDIV):
    mult = a
    logb = int(math.log2(b)) + 1
    ans = 1
    for i in range(logb):
        if b & (1 << i):
            ans *= mult
            ans %= ANSDIV
        mult *= mult
        mult %= ANSDIV
    return ans

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)
ANSDIV = 10 ** 9 + 7
N = int(input())

#事前準備
fac = [1] * (N + 1)
for i in range(2, N+1):
    fac[i] = fac[i-1] * i % ANSDIV
ifac = [1] * (N+1)
ifac[N] = logpow(fac[N], ANSDIV-2, ANSDIV)
for i in range(N-1, 1, -1):
    ifac[i] = ifac[i+1]*(i+1)%ANSDIV

def nCr(n, r, ANSDIV):
    return fac[n]*ifac[r]%ANSDIV*ifac[n-r]%ANSDIV

def calc(space, N):
    if space == 1:
        return logpow(2, N, ANSDIV)-1

    ans = 0
    for k in range(1, (N -1) // space + 2):
        ans += nCr(N - (k-1) * (space - 1), k, ANSDIV)
        ans %= ANSDIV
        
    return ans



for i in range(1, N+1):
    print(calc(i, N))

            
            