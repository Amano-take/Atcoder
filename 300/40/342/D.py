import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8
2 2 4 6 3 100 100 25
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N = int(input())
As = list(map(int, input().split()))

#eratstenes

def eratstenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    primes = []
    for i in range(n+1):
        if is_prime[i]:
            primes.append(i)
    return primes

primes = eratstenes(2 * 10 ** 3)
square_of_prime = [p ** 2 for p in primes]

def f(n):
    f = 0
    while square_of_prime[f] <= n:
        if n % square_of_prime[f] == 0:
            n //= square_of_prime[f]
        else:
            f += 1
    return n 
dic = ddict(int)
ans = 0
zeros = 0
for a in As:
    if a == 0:
        zeros += 1
    else:
        dic[f(a)] += 1
for v in dic.values():
    ans += v * (v-1) // 2
ans += zeros * (N - zeros)
ans += zeros * (zeros - 1) // 2
print(ans)
