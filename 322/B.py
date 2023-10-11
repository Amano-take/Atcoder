import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4
abc
aabc
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, readline().split())
S = list(input())
T = list(input())

if T[:N] == S:
    if T[M-N:] == S:
        print("0")
    else:
        print("1")
else:
    if T[M-N:] == S:
        print("2")
    else:
        print("3")