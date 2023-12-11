import sys
import io
import math
import itertools
sys.setrecursionlimit(10**8)
_INPUT = """\
4
2 3 4 1
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
Goal = sorted(A)
circulant = [[0] * 4 for _ in range(4)]
for i in range(N):
    a = A[i]
    g = Goal[i]
    if a == g:
        continue
    else:
        circulant[a-1][g-1] += 1

circuit = [[] for _ in range(3)]
for i, j, k, l in itertools.permutations(range(4), 4):
    diff = 0
    if i != 0:
        diff += 1
    if j != 1:
        diff += 1
    if k != 2:
        diff += 1
    if l != 3:
        diff += 1

    if diff == 0:
        continue
    else:
        circuit[diff-2].append([i, j, k, l])

ans = 0

for diff, c in enumerate(circuit):
    diff += 2
    for ijkl in c:
        i, j, k, l = ijkl
        vs = []
        if i != 0:
            vs.append(circulant[0][i])
        if j != 1:
            vs.append(circulant[1][j])
        if k != 2:
            vs.append(circulant[2][k])
        if l != 3:
            vs.append(circulant[3][l])
        
        v = min(vs)
        if v == 0:
            continue
        
        for index in range(4):
            circulant[index][ijkl[index]] -= v
        
        ans += v * (diff - 1)

print(ans)
