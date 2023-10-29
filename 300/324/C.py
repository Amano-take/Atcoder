import sys
import io
import math
import bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4
1000 500 700 2000
xxxo
ooxx
oxox
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
score = list(map(int, readline().split()))

playerscore = [0] * N
playerleft = []
for i in range(N):
    S = list(input())
    ssum = 0
    left = []
    for j, s in enumerate(S):
        if s == "o":
            ssum += score[j]
        else:
            left.append(score[j])
    playerscore[i] = ssum+i
    left.sort(reverse=True)
    playerleft.append(left)

target = max(playerscore)
if playerscore.count(target) >= 2:
    flag = True
else:
    flag = False

playercumsum = []
for left in playerleft:
    cumsum = [0] * (len(left)+1)
    for i in range(len(left)):
        cumsum[i+1] = left[i] + cumsum[i]
    playercumsum.append(cumsum)

for i in range(N):
    if playerscore[i] == target and not flag:
        print(0)
    else:
        index = bisect.bisect_left(playercumsum[i], target+1-playerscore[i])
        print(index)


