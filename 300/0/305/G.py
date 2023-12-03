import sys
import io
import math
import time
sys.setrecursionlimit(10**8)
_INPUT = """\
4 3
aab
bbab
abab
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N, M = map(int, readline().split())
banned = set()
for i in range(M):
    s = list(readline().strip())
    s.insert(0, "b")
    v = map(lambda x: str(ord(x) - ord("a")), s)
    v = "".join(v)
    banned.add(v[1:])
merge = []
for j in range(1 << 5, 1<<6):
    for i in range(1 << 5, 1 << 6):
        sum = (j-1) << (i.bit_length() - 1)
        sum += i
        sum = bin(sum)[3:]
        for x in range(1, 6):
            for y in (1, 7 - x):
                if sum[5 - x:5 + y] in banned:
                    merge.append((j, i))
                    break
            else:
                continue
            break
dpA = [[0] * 64 for _ in range((10 ** 18).bit_length() - 3)]
for i in range(1<<8, 1<<9):
    moji = bin(i)[3:]
    for b in banned:
        if moji.find(b) != -1:
            break
    else:
        end = int(moji[3:], 2)
        start = int(moji[:5], 2)
        dpA[0][end] += 1
        dpA[0][32+start] += 1
print(dpA[0])

