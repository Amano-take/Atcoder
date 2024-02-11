import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
50
"""
sys.stdin = io.StringIO(_INPUT)
ANSDIV = 10 ** 9 + 7
N = int(input())
pair = [0] * (N+1)
pair[1] = N
def calc(space, N):
    if space == 1:
        ans = 1
        for _ in range(N):
            ans *= 2
            ans %= ANSDIV
        return ans -1
    if 1 + space >  N:
        return N
    
    if 1 + 2 * space > N:
        if N % 2 == space % 2:
            a = (N - space) // 2
            a %= ANSDIV
            a *= N - space + 1
            a %= ANSDIV
            a += N
            a %= ANSDIV
            return a
        else:
            a = (N - space + 1)// 2
            a %= ANSDIV
            a *= N - space
            a %= ANSDIV
            a += N
            a %= ANSDIV
            return a
        
    ans = 0
    for s in range(1, N - space+1):
        ans += calc(space, N-space-s+1)
    return ans + N

for i in range(1, N+1):
    print(calc(i, N))
    

            