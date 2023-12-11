import sys
import io
import math
import bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
1000000000000
"""

sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(readline())
max = int((N // 12) ** (1/ 2))
#eratstenes
is_prime = [True] * (max + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(max ** (1 / 2)) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, max + 1, i):
        is_prime[j] = False
primes = []
for i in range(max + 1):
    if is_prime[i]:
        primes.append(i)
ans = 0
for a in range(len(primes)):
    if primes[a] ** 5 > N:
        break
    high = len(primes)
    for b in range(a+1, len(primes)):
        if primes[a]**2 * primes[b]**3 > N:
            break

        maxc = (N / (primes[a]**2 * primes[b])) ** (1/2)
        indexc = bisect.bisect_right(primes, maxc,hi=high)
        high = indexc
        ans += indexc - b - 1
print(ans)