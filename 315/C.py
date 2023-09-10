import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
4
4 10
3 2
2 4
4 12
"""
sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline
N = int(input())
FS = []
for _ in range(N):
    f, s = map(int, input().split())
    FS.append((f, s))

FS.sort(key=lambda x: x[1], reverse=True)
f0, s0 = FS.pop(0)
maxf = 0
maxd = 0
for f, s in FS:
    if maxf == 0 and f == f0:
        maxf = s // 2
    elif maxd == 0 and f != f0:
        maxd = s
    if maxf * maxd != 0:
        break

print(s0 + max(maxf, maxd))

