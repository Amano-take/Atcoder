import sys
import io
import math
from collections import deque, defaultdict as ddict
from itertools import permutations
sys.setrecursionlimit(10**8)
_INPUT = """\
8 4
fast
face
cast
race
fact
rice
nice
case
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
Ss = [readline().strip() for _ in range(N)]

def almostequal(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1

for P in permutations(range(N)):
    for i in range(N-1):
        if not almostequal(Ss[P[i]], Ss[P[i+1]]):
            break
    else:
        print("Yes")
        exit()
print("No")
