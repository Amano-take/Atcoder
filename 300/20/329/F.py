import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6 5
1 1 1 2 2 3
1 2
6 4
5 1
3 6
4 6
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()


N, Q = map(int, readline().split())
Cs = list(map(lambda x: set([int(x)]), readline().split()))
empty = set()
for i in range(Q):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    if len(Cs[b]) < len(Cs[a]):
        Cs[a] |= Cs[b]
        Cs[a], Cs[b] = Cs[b], Cs[a]
    else:
        Cs[b] |= Cs[a]
    Cs[a] = set()
    print(len(Cs[b]))     
    