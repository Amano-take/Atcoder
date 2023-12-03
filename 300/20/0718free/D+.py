n, t, m = map(int, input().split())
a, b = zip(*[map(int, input().split()) for _ in range(m)]) if m > 0 else ([], [])
ok = [all(map(lambda j: (i & j) != j, [(1 << (a[j]-1)) | (1 << (b[j]-1)) for j in range(m)])) for i in range(1 << n)]
dp = [[0] * (1 << n) for _ in range(t) ]
for i in filter(lambda i: i & 1 != 0 and ok[i], range(1 << n)):
    dp[0][i] = 1
MASK = (1 << n) - 1
for i in range(t-1):
    for j in range(1, 1 << n):
        if dp[i][j] == 0:
            continue
        rem = MASK ^ j
        now = rem
        clause = rem & -rem
        while now > 0:
            #{1, 2, 5},{3, 6}, {4, 7} == {1, 2, 5}, {4, 7}, {3, 6}
            # -> {1, 2, 5}, {4, 7} = 0に
            if ok[now] and (now & clause) != 0:
                dp[(i + 1)][j|now] += dp[i][j]
            now = (now - 1) & rem
print(dp)