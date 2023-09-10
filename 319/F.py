import sys
import io
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
13
9 7 11 7 3 8 1 13 11 11 11 6 13
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N = int(input())
A = list(map(int, readline().split()))
N = defaultdict(int)
P = defaultdict(int)
answer = 0

for position, alphabet in enumerate(A):
    
    if N[alphabet] != 0:
        n = N[alphabet]
        answer += (position - 1) * n - P[alphabet] - n*(n-1)//2
    N[alphabet] += 1
    P[alphabet] += position
    
print(answer)