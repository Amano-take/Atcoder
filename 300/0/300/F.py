import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
10 2 5
ooxxooooox
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
    
num_x = cumsum[-1]
tail = 0
X = -2
ans = 0
#尺取り
for i in range(N):
    headx = cumsum[-1] - cumsum[i]
    if X == -2:
        if K - headx > 0:
            X = (K - headx) // num_x
            rest = (K - headx) % num_x
        else:
            X = -1
            rest = K - cumsum[i]
        while True:
            if X >= M - 1:
                tail = N
                X = M - 2
                break
            if rest == 0 and S[tail] == "x":
                break
            else:
                if S[tail] == "x":
                    rest -= 1
                tail += 1
                if tail == N:
                    break
    
    if i > 0 and S[i-1] == "x" and not tail == N:
        rest = 1
        while True:
            if S[tail] == "x" and rest == 0:
                break
            elif S[tail] == "x":
                rest -= 1
            
            if tail == N - 1 and X < M-2:
                tail = 0
                X += 1
            elif tail == N - 1:
                tail = N
                break
            else:
                tail += 1
            
    
    else:
        pass
    print(i, tail, X)
    ans = max(ans, X * N + tail + N - i)

print(ans)