import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
200000 314 318
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M, P = map(int, input().split())
print(int((N-M) / P + 1))