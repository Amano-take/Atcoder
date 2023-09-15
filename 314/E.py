import sys
import io
import random
sys.setrecursionlimit(10**8)
_INPUT="""\
3 14
100 2 5 9
50 4 1 2 4 8
70 5 2 4 2 8 8
"""
sys.stdin=io.StringIO(_INPUT)
readline = sys.stdin.readline

N, M = map(int, input().split())
rou = []
roulett = []


for i in range(N):
    c, p, *num = map(int, readline().split())
    roulett.append(num)
    exp = sum(num) / p
    costp = exp / c
    rou.append((exp, costp, c, i))

rou.sort(key=lambda x: -x[1])
ans = 0
for _ in range(100):
    rest = M
    while rest > 0:
        for exp, costp, c, i in rou:
            if exp <= rest:
                ans += c
                rest -= random.choice(roulett[i])
                break
    
print(ans / 100)
            

