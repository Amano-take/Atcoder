import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
4 3
aaa
aaa
abc
abd
"""
sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline

H, W = map(int, input().split())
remainH = [1] * H
remainW = [1] * W
cookie = [[] for _ in range(H)]
for i in range(H):
    cookie[i] = list(input().strip())


stop = False

while not stop:
    if sum(remainH) == 1:
        break
    if sum(remainW) == 1:
        break
    flagH = [1] * H
    flagW = [1] * W
    stopH = True
    stopW = True
    to_judgeH = 0
    to_judgeW = 0
    ffH = False
    FFW = False

    for h in range(H):
        if not remainH[h]:
            continue
        if not ffH:
            to_judgeH = h 
            ffH = True
        for w in range(W):
            if not remainW[w]:
                continue
            if not FFW:
                to_judgeW = w 
                FFW = True

            if cookie[h][w] != cookie[h][to_judgeW]:
                flagH[h] = 0
            if cookie[h][w] != cookie[to_judgeH][w]:
                flagW[w] = 0
        
    for i, h in enumerate(flagH):
        if not remainH[i]:
            continue
        if h:
            if remainH[i]:
                remainH[i] = 0
                stopH = False
            
    for i, w in enumerate(flagW):
        if not remainW[i]:
            continue
        if w:
            if remainW[i]:
                remainW[i] = 0
                stopW = False
    stop = stopH and stopW

print(sum(remainH) * sum(remainW))