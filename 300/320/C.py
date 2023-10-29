import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
10
1937458062
8124690357
2385760149
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
slot = [[] for _ in range(3)]
for i in range(3):
    slot[i] = list(map(int, list(readline().strip())))

numlist = [[[] for _ in range(10)] for _ in range(3)]
for i in range(3):
    for index, s in enumerate(slot[i]):
        numlist[i][s].append(index)
ans = math.inf
for i in range(10):
    a = [[] for _ in range(3)]
    for j in range(3):
        a[j] = numlist[j][i]
        if len(a[j]) < 3:
            a[j].extend([i+N for i in a[j]])
        if len(a[j]) < 3:
            a[j].extend([i+2*N for i in a[j]])
        if len(a[j]) < 1:
            break
        a[j] = a[j][0:3]
    else:
        a.sort()
        t1 = a[2][0]
        if a[1][0] == t1:
            t2 = a[1][1]
        else:
            t2 = a[1][0]

        if a[0][0] == t1 or a[0][0] == t2:
            if a[0][1] == t1 or a[0][1] == t2:
                t3 = a[0][2]
            else:
                t3 = a[0][1]
        else:
            t3 = a[0][0]
        ans = min(ans, max(t1, t2, t3))
if ans == math.inf:
    ans = -1
print(ans)