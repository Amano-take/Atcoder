import sys
import io
from collections import deque
sys.setrecursionlimit(10**8)

_INPUT = """\
5 5
1 5
1 5
1 5
1 5
1 5
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, readline().split()) 
Opener = []
Can0 = []
Can1 = []
for i in range(N):
    t, x = map(int, readline().split())
    if t==0:
        Can0.append(x)
    elif t==1:
        Can1.append(x)
    else:
        Opener.append(x)
    
Opener.sort(reverse=True)
Can0.sort(reverse=True)
Can1.sort(reverse=True)
Can1 = deque(Can1)
Opener = deque(Opener)

CumX0 = [0]
for i in range(len(Can0)):
    CumX0.append(CumX0[-1]+Can0[i])
CumX1 = [0]
canOpen = 0
for i in range(M):
    if canOpen == 0 and len(Opener) != 0:
        CumX1.append(CumX1[-1])
        canOpen += Opener.popleft()
    elif len(Can1) != 0 and canOpen != 0:
        canOpen -= 1
        CumX1.append(CumX1[-1] + Can1.popleft())
    else:
        CumX1.append(CumX1[-1])       
ans = 0

for i in range(min(len(CumX0), M+1)):
    ans = max(ans, CumX0[i] + CumX1[M-i])
print(ans)