

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extgcd(b, a % b)
    y -= a // b * x
    return g, x, y
 
N = int(input())
A, B, C = sorted(map(int, input().split()))[::-1]
 
lim = 10000
ans = lim
g, x, y = extgcd(B, C)
for i in range(lim):
    rem = N - A * i
    if rem >= 0 and rem % g == 0:
        j = x * (rem // g)
        k = y * (rem // g)
        tk = k % (B // g)
        j -= (tk - k) // (B // g) * (C // g)
        k = tk
        if j >= 0:
            ans = min(ans, i + j + k)
 
print(ans)
def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extgcd(b, a % b)
    y -= a // b * x
    return g, x, y

N = int(input())
A, B, C = sorted(map(int, input().split()))[::-1]

lim = 10000
ans = lim
g, x, y = extgcd(B, C)
for i in range(lim):
    rem = N - A * i
    if rem >= 0 and rem % g == 0:
        j = x * (rem // g)
        k = y * (rem // g)
        tk = k % (B // g)
        j -= (tk - k) // (B // g) * (C // g)
        k = tk
        if j >= 0:
            ans = min(ans, i + j + k)

print(ans)
