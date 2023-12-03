import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
Takahashi Chokudai
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S, _ = input().split()
print(S + " san")