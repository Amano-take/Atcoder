import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
30
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()

N = int(input())
Ds = list(map(int, readline().split()))
ans = 0
for i, d in enumerate(Ds):
    month = i+1
    for day in range(1, d+1):
        a = set()
        if month >= 10:
            a.add(month//10)
        a.add(month % 10)
        if day >= 10:
            a.add(day//10)
        a.add(day % 10)

        if len(a) == 1:
            ans += 1
print(ans)