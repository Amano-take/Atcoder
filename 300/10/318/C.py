import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
3 1 10
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
F.extend([0] * D * 2)

i = 0
tickets = 0

while True:
    sums = 0
    for index in range(i, i+D):
        sums += F[index]
    if sums > P:
        tickets += 1
    else:
        rest = sums + sum(F[i+D:])
        print(tickets*P + rest)
        break
    i += D
