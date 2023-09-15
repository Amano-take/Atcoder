import sys
import io
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT="""\
35
TheQuickBrownFoxJumpsOverTheLazyDog
10
2 0 a
1 19 G
1 13 m
1 2 E
1 21 F
2 0 a
1 27 b
3 0 a
3 0 a
1 15 i
"""
sys.stdin=io.StringIO(_INPUT)

N = int(input())
ans = list(input())
Q = int(input())
read = sys.stdin.readlines()

final = 0
q = []
for i, s in enumerate(read):
    t, x, c = s.split()
    q.append((t, x, c))
    if t != '1':
        final = i

for i, s in enumerate(q):
    t, c, x = s
    c = int(c)
    if t == "1":
        ans[c-1] = x
    elif t == "2" and i == final:
        ans = list("".join(ans).lower())
    elif t == "3" and i == final:
        ans = list("".join(ans).upper())
print("".join(ans))