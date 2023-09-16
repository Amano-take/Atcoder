import sys
import io
import itertools
import math

sys.setrecursionlimit(10**8)
_INPUT = """\
3 6 7
1 9 7
5 7 5
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
const = []
CL = [input().split() for _ in range(3)]
for i in range(3):
    if CL[i][1] == CL[i][2]:
        const.append((i*3 + 1, i*3 + 2, i*3))
    elif CL[i][0] == CL[i][1]:
        const.append((i*3, i*3+1, i*3+2))
    elif CL[i][0] == CL[i][2]:
        const.append((i*3, i*3+2, i*3+1))

    if CL[1][i] == CL[2][i]:
        const.append((3 + i, 6+i, i))
    elif CL[0][i] == CL[1][i]:
        const.append((i, 3 + i, 6+i))
    elif CL[0][i] == CL[2][i]:
        const.append((i, 6+i, 3+i))

if CL[0][2] == CL[1][1]:
    const.append((2, 4, 6))
elif CL[0][2] == CL[2][0]:
    const.append((2, 6, 4))
elif CL[1][1] == CL[2][0]:
    const.append((4, 6, 2))

if CL[2][2] == CL[1][1]:
    const.append((8, 4, 0))
elif CL[0][0] == CL[2][2]:
    const.append((0, 8, 4))
elif CL[1][1] == CL[0][0]:
    const.append((4, 0, 8))


ho = 0
for k in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8]):
    for c1, c2, c3 in const:
        i1 = k.index(c1)
        i2 = k.index(c2)
        i3 = k.index(c3)
        if i1 < i3 and i2 < i3:
            ho += 1
            break
print((math.factorial(9) - ho)/ math.factorial(9))
