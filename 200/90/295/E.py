import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
DIV = 998244353
sys.setrecursionlimit(10**8)
_INPUT = """\
3 5 2
2 0 4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M, K = map(int, input().split())
As = list(map(int, input().split()))
Bs = []
zeronum = 0
for a in As:
    if a == 0:
        zeronum += 1
        continue
    Bs.append(a)

Bs.sort()

fact = [1]
for i in range(1, N+1):
    fact.append((fact[-1] * i) % DIV)
INVfact = [1]
for i in range(1, N+1):
    INVfact.append((INVfact[-1] * pow(i, -1, DIV)) % DIV)
ALLprob = pow(M, zeronum, DIV)
INVprob = pow(ALLprob, -1, DIV)


def comb(n, k):
    return (fact[n] * INVfact[k] * INVfact[n-k]) % DIV

def prob(pibot, r):
    ans = 0
    for i in range(r, zeronum+1):
        
        proba = INVprob
        proba *= comb(zeronum, i) * pow(M - pibot + 1, i, DIV)
        proba %= DIV
        proba *= pow(pibot - 1, zeronum - i, DIV)
        proba %= DIV
        ans += proba
    return ans
ans = 0

#式変形をすれば、for文一つ消せる
for Knum in range(1, M+1):
    l = bisect.bisect_left(Bs, Knum)
    exitB = len(Bs) - l
    need = max(0, N - K  + 1 - exitB)
    if need > zeronum:
        break
    ans += prob(Knum, need)
    ans %= DIV

print(ans)
            
            
