import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
4 2 3
5 4
6 6
3 1
7
13
0
710511029
136397527
763027379
644706927
447672230
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N, X, Y = map(int, input().split())
buss = []
for k in range(N-1):
    P, T = map(int, readline().split())
    buss.append((P, T))

dev = 8*7*5*3
ans = [0] * dev
for i in range(dev):
    t1 = i+X
    for p, t in buss:
        if t1 % p == 0:
            t1 += t
        else:
            t1 = ((t1 // p) + 1) * p + t
    ans[i] = t1+Y - i
Q = int(input())
for j in range(Q):
    time = int(readline().strip())
    print(time + ans[time%dev])
