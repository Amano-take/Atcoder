import sys
import io
import math
import bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
10 1 1
xxxxxxxxxx
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M, K = map(int, readline().split())
S = list(readline().strip())
cumsum = [0]
for i in range(N):
    if S[i] == "x":
        cumsum.append(cumsum[-1] + 1)
    else:
        cumsum.append(cumsum[-1])
    
ans = 0

for head in range(N):
    fblockx = cumsum[-1] - cumsum[head]
    if fblockx > K:
        X = -1
        #BAG
        tail = bisect.bisect_right(cumsum, K + cumsum[head]) - 1
    else:
        X = (K - fblockx) // (cumsum[-1])
        rest = (K - fblockx) % (cumsum[-1])
        if X >= M -1:
            X = M - 2
            tail = N
        else:
            tail = bisect.bisect_right(cumsum, rest) - 1
    ans = max(ans, X*N + tail - head + N)

print(ans)