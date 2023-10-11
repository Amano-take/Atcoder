import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
3
ACB
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
S = list(input())
i = 0
while i + 2 < N:
    if S[i:i+3] == ["A", "B", "C"]:
        print(i+1)
        break
    i += 1
else:
    print("-1")
