import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
2
takahashi 1000000000
aoki 999999999
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
people = [ readline().split() for _ in range(N)]
minage = min(enumerate(people), key=lambda x: int(x[1][1]))[0]
for i in range(minage, minage + N):
    index = i % N
    print(people[index][0])