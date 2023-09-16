import sys
import io
sys.setrecursionlimit(10**8)



N = int(input())

def brackets(N):
    if N % 2 != 0:
        return set()
    if N == 2:
        return {2}

    ans = set(map(lambda b: ( 1 << (N-1)) + (b << 1), brackets(N-2)))

    for i in range(2, N-1, 2):
        for br in brackets(i):
            ans |= set(map(lambda b: br + (b << i), brackets(N-i)))

    return ans

ans = sorted(list(brackets(N)), reverse=True)
for bits in ans:
    print(str(format(bits, 'b')).replace('1', '(').replace('0', ')'))
    