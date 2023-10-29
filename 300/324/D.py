import sys
import io
import math
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT = """\
1
1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

def x22(x:int):
    l = 0
    r = x.bit_length()+1
    while r != l + 1:
        mid = (l + r) // 2
        mask = (1 << mid) - 1
        if x & mask == 0:
            l = mid
        else:
            r = mid
    return l, x >> l

N = int(input())
slime = ddict(int)
for i in range(N):
    S, C = map(int, readline().split())
    r, x = x22(S)
    slime[x] += (1 << r) * C
ans = 0
for k, value in slime.items():
    ans += bin(value).count("1")
print(ans)
