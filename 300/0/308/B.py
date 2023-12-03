import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
3 2
red green blue
blue red
800 1600 2800
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M  = map(int, readline().split())
Cs = list(readline().split())
Ds = list(readline().split())
Ps = list(map(int, readline().split()))
ans = 0
for c in Cs:
    try:
        i = Ds.index(c)
        ans += Ps[i+1]
    except:
        ans += Ps[0]
print(ans)