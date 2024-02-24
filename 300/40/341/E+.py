N, Q = map(int, input().split())
S = input()

BIT = [0] * (N + 1)
def update(i, x):
    while i < len(BIT):
        BIT[i] += x
        i += (i & -i)

def bit_sum(i):
    res = 0
    while i > 0:
        res += BIT[i]
        i -= (i & -i)
    return res

A = [0] * (N+1)
for i in range(N-1):
    if S[i] == S[i+1]:
        A[i+1] = 1
        update(i+1, 1)

for _ in range(Q):
    q, l, r = map(int, input().split())
    if q == 1:
        if l > 1: 
            update(l-1, -1 if A[l-1] else 1)
            A[l-1] ^= 1
        if r < N: 
            update(r, -1 if A[r] else 1)
            A[r] ^= 1
    else:
        yes = (bit_sum(r-1) - bit_sum(l-1)) == 0
        if yes: print("Yes")
        else: print("No")
        