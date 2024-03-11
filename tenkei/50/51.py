import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product

inf = float("inf")

input = lambda: sys.stdin.readline().strip()

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

A_pref = A[: N // 2]
A_suff = A[N // 2 :]

dic_pref = [ddict(int) for _ in range(len(A_pref) + 1)]
for i in range(1 << (len(A_pref))):
    cnt = 0
    num = 0
    for j in range(len(A_pref)):
        if (i >> j) & 1:
            cnt += A_pref[j]
            num += 1
    dic_pref[num][cnt] += 1
for i in range(len(A_pref) + 1):
    lis = []
    for k, v in dic_pref[i].items():
        lis.append((k, v))
    lis.sort()
    dic_pref[i] = lis


dic_suff = [[] for _ in range(len(A_suff) + 1)]
for i in range(1 << (len(A_suff))):
    cnt = 0
    num = 0
    for j in range(len(A_suff)):
        if (i >> j) & 1:
            cnt += A_suff[j]
            num += 1
    dic_suff[num].append(cnt)
for i in range(len(A_suff) + 1):
    dic_suff[i].sort()

ans = 0
for i in range(len(A_pref) + 1):
    if i > K:
        break
    if K - i >= len(dic_suff):
        continue
    dic = dic_suff[K - i]
    for k, v in dic_pref[i]:
        idx = bisect.bisect_right(dic, P - k)
        if idx == 0:
            continue
        ans += v * idx
print(ans)
