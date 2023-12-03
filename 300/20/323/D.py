import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
4
4320
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
ST = input()
S = list(ST)
cs = []
for i in range(10):
    cs.append(S.count(str(i)))

if int(ST) == 0:
    print(1)
    exit()
ans = 0
sq = []
i = 1
while True:
    if i*i > 10**N - 1:
        break
    sq.append(i*i)
    i+=1
for num in sq:
    dig = len(str(num))
    cl = list(str(num))

    if (N - dig) + cl.count(str(0)) != cs[0]:
        continue
    for i in range(1, 10):
        ci = cl.count(str(i))
        if ci != cs[i]:
            break
    else:
        ans += 1

print(ans)
