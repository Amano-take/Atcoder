import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
#anti case
_INPUT = """\
3 5
1 1 2 3 4
1 2 3 4 1
6 7 8 9 0
1 2 3 4 1
1 1 2 3 4
6 7 8 9 0
"""
#行が同じかどうかの判定に集合を使っていることがミスの原因
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
H, W = map(int, input().split())
gridA = [list(map(int, input().split())) for _ in range(H)]
gridB = [list(map(int, input().split())) for _ in range(H)]
goalrawset = [ddict(int) for _ in range(H)]
goalcolset = [ddict(int) for _ in range(W)]
arawset = [ddict(int) for _ in range(H)]
acolset = [ddict(int) for _ in range(W)]
for i in range(H):
    for j in range(W):
        goalrawset[i][gridB[i][j]] += 1
        goalcolset[j][gridB[i][j]] += 1
        arawset[i][gridA[i][j]] += 1
        acolset[j][gridA[i][j]] += 1

def issame(da, db):
    for i in da:
        if da[i] != db[i]:
            return False
    return True

ans = 0
circular = []
used = [False for _ in range(H)]
for i in range(H):
    for j in range(H):
        if issame(goalrawset[j], arawset[i]) and used[j] == False:
            circular.append(j)
            used[j] = True
            break

if all(used) == False:
    print(-1)
    exit()



for i in range(H-1):
    for j in range(i+1, H):
        if circular[i] > circular[j]:
            ans += 1

    
circular = []
used = [False for _ in range(W)]
for i in range(W):
    for j in range(W):
        if issame(acolset[i], goalcolset[j]) and used[j] == False:
            circular.append(j)
            used[j] = True


if all(used) == False:
    print(-1)
    exit()

for i in range(W-1):
    for j in range(i+1, W):
        if circular[i] > circular[j]:
            ans += 1
    
print(ans)