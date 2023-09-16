import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
6 5
2 5
1 4
1 3
5 6
2 3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, input().split())
answer = M * (M-1) // 2
l = [0] * N
V1 = [0] * N
V2 = [0] * N
for _ in range(M):
    p, q = map(lambda x: int(x) - 1, readline().split())
    l[p] += 1
    l[q] += 1
    V1[p] += 1
    V2[q] += 1

#余事象１
mi1 = 0
for k in l:
    mi1 += k * (k-1) // 2

#余事象2
mi2 = 0
for i in range(1, N):
    V2[i] += V2[i-1]
for j in range(1, N):
    mi2 += V1[j] * V2[j-1]

#余事象3
