import sys
import io
from collections import defaultdict

sys.setrecursionlimit(10**8)
_INPUT="""\
15
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32
"""
sys.stdin=io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
dict = defaultdict(int)

for inter in range(0, N):
    for start in range(0, 2*N - (2 * inter) - 1):
        if inter == 0:
            dict[(start, start+1)] = abs(A[start] - A[start+1])
        else:
            min = abs(A[start] - A[start+inter*2+1]) + dict[(start+1, start+inter*2)]
            for num in range(0, inter):
                p = dict[(start, start+2*num+1)] + dict[(start+2*num+2, start+2*inter+1)]
                if p < min:
                    min = p
            dict[(start, start+2*inter+1)] = min

print(dict[(0, 2*N-1)]) 