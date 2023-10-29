import sys
import io
import itertools
from functools import reduce
sys.setrecursionlimit(10**8)
_INPUT = """\
....
###.
.#..
....
....
.###
.##.
....
..#.
.##.
.##.
.##.
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
A = [list(input()) for _ in range(4)]
B = [list(input()) for _ in range(4)]
C = [list(input()) for _ in range(4)]
for i in range(4):
    A[i] = list(map(lambda x: 0 if x=="." else 1, A[i]))
    B[i] = list(map(lambda x: 0 if x=="." else 1, B[i]))
    C[i] = list(map(lambda x: 0 if x=="." else 1, C[i]))
zuA = [A]
zuB = [B]
zuC = [C]
preA = A
preB = B
preC = C
for i in range(3):
    rotatedA = list(map(lambda x: list(x), (zip(*preA[::-1]))))
    rotatedB = list(map(lambda x: list(x),(zip(*preB[::-1]))))
    rotatedC = list(map(lambda x: list(x), zip(*preC[::-1])))
    zuA.append(rotatedA)
    zuB.append(rotatedB)
    zuC.append(rotatedC)
    preA = rotatedA
    preB = rotatedB
    preC = rotatedC

def detect_pos(P):
    t = 3
    b = 0
    l = 3
    r = 0
    for i in range(4):
        if sum(P[i]) != 0:
            t = min(t, i)
            b = max(b, i)
    for j in range(4):
        tmp = 0
        for i in range(4):
            tmp += P[i][j]
        if tmp != 0:
            l = min(l, j)
            r = max(r, j)
    return t, b, l, r

def generate(P):
    t, b, l, r = detect_pos(P)
    NP = [[0] * 4 for _ in range(4)]
    for i in range(b-t+1):
        for j in range(r-l+1):
            NP[i][j] = (P[i+t][j+l])
    return NP

zuA = list(map(generate, zuA))
zuB = list(map(generate, zuB))
zuC = list(map(generate, zuC))

lenAll = reduce(lambda acc, cur: acc+sum(cur), zuA[0]+zuB[0]+zuC[0], 0)

if lenAll != 16:
    print("No")
    exit()

for sa, sb, sc in itertools.product(range(16), repeat=3):
        for tb, tc in itertools.product(range(4), repeat=2):
            li = [(zuA[0],sa), (zuB[tb], sb), (zuC[tc],sc)]
            base = [[0] * 7 for _ in range(7)]
            for zu, p in li:
                y = p // 4
                x = p % 4
                for i, retu in enumerate(zu):
                    for j, z in enumerate(retu):
                        base[y+i][x+j] += z
            
            for i, j in itertools.product(range(4), repeat=2):
                if base[i][j] != 1:
                    break
            else:
                print("Yes")
                exit()
print("No")
                