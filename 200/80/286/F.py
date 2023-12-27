import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
def extendEuclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = extendEuclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q
    
def crt1(PairPrimes, PairRest):
    m1, m2 = PairPrimes
    r1, r2 = PairRest
    x, y, q = extendEuclid(m1, m2)
    _, _, _q = extendEuclid(r1, r2)
    assert _q % q == 0
    if q != 1:
        return crt1([m1 // q, m2 // q], [r1 // q, r2 // q])
    else:
        return (r1 * y * m2 + r2 * x * m1) % (m1 * m2), m1 * m2

def crt(PairPrimes, PairRest):
    assert len(PairPrimes) == len(PairRest)
    rest, mod = crt1(PairPrimes[:2], PairRest[:2])
    for i in range(2, len(PairPrimes)):
        rest, mod = crt1([mod, PairPrimes[i]], [rest, PairRest[i]])
    return rest, mod

inf = float("inf")
sys.setrecursionlimit(10**8)
input=lambda: sys.stdin.readline().strip()
Primes = [4, 9, 5, 7, 11, 13, 17, 19, 23]
target = []
ans = []
start = 1
for p in Primes:
    temp = []
    target.append(start)
    for i in range(start+1, start + p):
        temp.append(i)
    temp.append(start)
    ans.extend(temp)
    start = start + p
print(sum(Primes))
print(*ans)
sys.stdout.flush()
Bs = list(map(int, input().split()))
rest = []
for t in target:
    rest.append(Bs[t-1] - t)
ans = crt(Primes, rest)
print(ans[0])
sys.stdout.flush()
    