import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
1
a
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N = int(input())
S = list(readline())
for i in range(len(S) - 1):
    if S[i] == "a" and S[i+1] == "b":
        print("Yes")
        exit()
    elif S[i] == "b" and S[i+1] == "a":
        print("Yes")
        exit()
print("No")