import sys
import io
import math
import itertools

sys.setrecursionlimit(10**8)
_INPUT = """\
5
ab
ccef
da
a
fe
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
Ss = [readline().strip() for _ in range(N)]
for i, j in itertools.permutations(range(N), 2):
    x = Ss[i] + Ss[j]
    if x == "".join(reversed(x)):
        print("Yes")
        exit()
print("No")
set()
