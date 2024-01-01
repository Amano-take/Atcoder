import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
2023
63
1059872604593911
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
def issquare(n):
    return int(n**0.5)**2 == n

is_prime = [True] * ( 3 *  10**6+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(3 * 10**6**0.5)+1):
    if not is_prime[i]:
        continue
    for j in range(i*2, 3 * 10**6+1, i):
        is_prime[j] = False
primes = []
for i in range(3 * 10**6+1):
    if is_prime[i]:
        primes.append(i)

for i in range(N):
    n = int(input())
    #n = p**2 * q (p: prime, q:prime)
    for p in primes:
        if n % p == 0:
            q = n // p
            if issquare(q):
                print(int(q**0.5), p)
                break
            elif q % p == 0:
                print(p, q//p)
                break
            