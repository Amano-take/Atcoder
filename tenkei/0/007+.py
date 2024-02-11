from bisect import bisect_left

# 無限大を表す値
INF = 2 ** 60

# 入力
N = int(input())
A = list(map(int, input().split()))

# ソートしておく
A.sort()

# 各クエリに答える
Q = int(input())
for _ in range(Q):
    B = int(input())

    # A[j] >= B となる最小の j を求める
    j = bisect_left(A, B)

    # A[j] と A[j-1] を比較する
    res = INF
    if j < N:
        res = min(res, abs(B - A[j]))
    if j > 0:
        res = min(res, abs(B - A[j-1]))

    print(res)