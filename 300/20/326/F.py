import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, X, Y = map(int, readline().split())
As = list(map(int, readline().split()))
cand = set()
cand.add((X, Y))
for i in range(N-1, -1, -1):
    temp = set()
    for p, s in cand:
        if i % 2 == 0:
            x = p[0]
            y = p[1] + As[i]
            temp.add(((x, y), s+"u"))
            temp.add(((x, y-As[i] * 2), s+"d"))
        else:
            x = p[0] + As[i]
            y = p[1]
            temp.add(((x, y))
            temp.add((x - As[i] * 2, y))
    cand = temp
if (0, 0) in cand:
    print("Yes")
