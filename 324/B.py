import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
7
-oxoxox
x-xxxox
oo-xoox
xoo-ooo
ooxx-ox
xxxxx-x
oooxoo-
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
result = [0] * N
def temp(x):
    if x == "x":
        return -1
    elif x == "o":
        return 1
    else:
        return 0
for i in range(N):
    B = list(input())
    win = 0
    for b in B:
        if b == "o":
            win += 1
    result[i] = (win, i)

result.sort(key=lambda x: x[0], reverse=True)
ans = []
for r in result:
    ans.append(r[1]+1)
print(*ans)


    