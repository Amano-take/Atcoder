import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
86410
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = input()
pre = 10
for n in N:
    a = int(n)
    if a >= pre:
        print("No")
        break
    pre = a
else:
    print("Yes")