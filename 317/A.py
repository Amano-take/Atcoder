import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
10 500 999
38 420 490 585 613 614 760 926 945 999
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, H, X = map(int, input().split())
PL = list(map(int, input().split()))
for i, p in enumerate(PL):
    if H + p >= X:
        print(i+1)
        break
