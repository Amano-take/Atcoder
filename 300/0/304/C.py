import sys
import io
import math
from collections import deque
sys.setrecursionlimit(10**8)
_INPUT = """\
4 5
2 -1
3 1
8 8
0 5
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, D = map(int, readline().split())
X = [list(map(int, readline().split())) for _ in range(N)]
infection = set([0])
queue = deque([0])
while len(queue) > 0:
    pi  = queue.pop()
    px, py = X[pi]
    for i, (x, y) in enumerate(X):

        if i not in infection and (px-x) ** 2 + (py-y)** 2 <= D**2:
            infection.add(i)
            queue.append(i)
for i in range(N):
    if i in infection:
        print("Yes")
    else:
        print("No")
