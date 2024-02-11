import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
5 5
1
2
3
4
5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, Q = map(int, input().split())
balls = [i for i in range(1, N+1)]
nums = [i for i in range(1, N+1)]

for _ in range(Q):
    x = int(input())
    if x == balls[-1]:
        ballnum = balls[N - 2]
        nums[x-1] = N - 1
        nums[ballnum-1] = N
        balls[N - 2], balls[N - 1] = balls[N - 1], balls[N - 2]

    else:
        index = nums[x-1]
        ballnum = balls[index]
        nums[x-1] = index + 1
        nums[ballnum - 1] = index
        balls[index], balls[index - 1] = balls[index - 1], balls[index]
print(*balls)