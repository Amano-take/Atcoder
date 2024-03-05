import sys
import random

input = sys.stdin.readline
rd = random.randint(10 ** 9, 2 * 10 ** 9)

n,l,d = map(int, input().split())
# Y获得的数字的概率
p = [0] * (l + d + 1)
p[0] = 1
cur = 1 / d
for i in range(1,l + d + 1):
    if i > d:
        cur -= p[i - d - 1] / d
    p[i] = cur
    if i < l:
        cur += p[i] / d
# 计算X获胜概率
X = [0] * (n + 1)
choose = 0
sum_y = 0
sum_x = 0
for i in range(n,-1,-1):
    # 必胜
    if i > l + d:
        X[i] = 1
    else:
        if i >= l:
            choose += p[i]
        X[i] = max((sum_x - sum_y)/d,1 - choose)
    sum_x += X[i]
    if i + d <= n:
        sum_y += X[i + d]
print(X[0])