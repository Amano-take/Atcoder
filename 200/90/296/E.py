import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5
2 3 4 5 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
As = list(map(int, input().split()))
#i transfer to As[i] in a step.
transition = [0] * N
for a in As:
    transition[a-1] += 1

queue = deque()
for i in range(N):
    if transition[i] == 0:
        queue.append(i)

while len(queue):
    i = queue.popleft()
    transition[As[i]-1] -= 1
    if transition[As[i]-1] == 0:
        queue.append(As[i]-1)

print(N - transition.count(0))

