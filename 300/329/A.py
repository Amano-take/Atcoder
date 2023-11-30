import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
ABC
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
print(*list(readline()))