from functools import cmp_to_key
def cmp(a, b):
    x, y, i = a
    xx, yy, ii = b
    s = x * yy - y * xx
    return 1 if s > 0 else -1 if s < 0 else 0
N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a, a + b, i))
X.sort(key = cmp_to_key(cmp))
print(*[i + 1 for x, y, i in X])