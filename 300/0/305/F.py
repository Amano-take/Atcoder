import sys
import io
import math
from collections import deque
sys.setrecursionlimit(10**8)
readline=sys.stdin.readline

N, M = map(int, readline().split())
ex = set([1])
stack = deque([1])
for _ in range(2 * N + 1):
    inp = readline().split()
    if len(inp) == 1:
        exit()
    else:
        k, *vs = map(int, inp)

    if N in vs:
        print(N)
        exit()
        continue

    for v in vs:
        if v not in ex:
            ex.add(v)
            stack.append(v)
            print(v)
            break
    else:
        stack.pop()
        v = stack[-1]
        print(v)
    sys.stdout.flush()