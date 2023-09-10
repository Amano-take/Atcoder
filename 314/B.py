import sys
import io
sys.setrecursionlimit(10**8)
_INPUT="""\
3
1
1
1
2
1
3
0
"""
sys.stdin=io.StringIO(_INPUT)
N = int(input())
kake = []
Clist = []
for i in range(N):
    C = int(input())
    Clist.append(C)
    kake.append(list(map(int, input().split())))
X = int(input())
ans = []
minc = 100
for index, p in enumerate(kake):
    for s in p:
        if s == X:
            ci = Clist[index]
            if ci < minc:
                minc = ci
            ans.append((ci, index))
final = []
for c, an in ans:
    if c == minc:
        final.append(an+1) 

print(len(final))
if len(final)!=0:
    print(*final)
else:
    print()
