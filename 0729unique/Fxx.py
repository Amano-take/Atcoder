import sys
import io
import math
import bisect
sys.setrecursionlimit(10**8)

_INPUT = """\
12 6
2 2
0 1
0 9
1 3
1 5
1 3
0 4
2 1
1 8
2 1
0 1
0 4
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split()) 
WCAN = []
CAN = []
CUT = []
ans = 0
for i in range(N):
    t, x = map(int, input().split())
    if t==0:
        WCAN.append(x)
    elif t==1:
        CAN.append(x)
    else:
        CUT.append(x)
    
WCAN.sort(reverse=True)
CAN.sort(reverse=True)
CUT.sort(reverse=True)

while M != 0:

    if len(CUT) == 0:
        ans += sum(WCAN[0:min(M, len(WCAN))])
        break

    cancat = CUT[0]
    cutting = 0
    indexw = 0
    indexc = 0
    for _ in range(M-1):
        if cancat == 0:
            break
        if indexw == len(WCAN):
            cutting += CAN[indexc]
            indexc += 1
            cancat -= 1
            continue
        if indexc == len(CAN):
            cutting += WCAN[indexw]
            indexw += 1
            continue
        if WCAN[indexw] >= CAN[indexc]:
            cutting += WCAN[indexw]
            indexw += 1
        else:
            cutting += CAN[indexc]
            indexc += 1
            cancat -= 1
    sumcut = indexw + indexc
    no_cutting = sum(WCAN[0:sumcut+1])

    if cutting >= no_cutting:
        ans += cutting
        CUT = CUT[1:]
        WCAN = WCAN[indexw:]
        CAN = CAN[indexc:]
        M -= sumcut + 1

    else:
        ans += no_cutting
        WCAN = WCAN[sumcut+1:]
        M -= sumcut+1


print(ans)
