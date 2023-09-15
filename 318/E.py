
import sys
import io
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
5
1 2 1 3 2
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
di = defaultdict(int)
ans = 0
for i, v in enumerate(L):
    
    di[v] += 1
