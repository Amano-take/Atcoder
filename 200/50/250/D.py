import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
250
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
ans = 0
N = int(input())
#エラトステネスの篩
def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
    return [i for i in range(n+1) if prime[i]]

primes = sieve(10 ** 6)

for i, p in enumerate(primes):
    if p == 2: 
        continue
    div = N // (p ** 3)
    if div < 2:
        break
    ans += min(i, bisect.bisect_right(primes, div))

print(ans)