import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
aaabbbbcccc
6
2 aa aaa
2 dd ddd
2 ab aabb
4 bbaa bbbc bbb bbcc
2 cc bcc
3 ccc cccc ccccc
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
T = input()
N = int(input())

import collections

def create_bad_calacter_heuristic_table(t):
    table = collections.defaultdict(lambda: -1)
    for k, c in enumerate(t):
        table[c] = k
    return table


def create_good_suffix_heuristic_table(t):
    f = [0] * (len(t) + 1)
    j = len(t) + 1
    f[len(t)] = j
    for k in reversed(range(1, len(t) + 1)):
        while j <= len(t) and t[k - 1] != t[j - 1]:
            j = f[j]
        f[k - 1] = j - 1
        j -= 1

    table = [0] * (len(t) + 1)
    for k in reversed(range(1, len(t) + 1)):
        j = f[k]
        while j <= len(t) and t[k - 1] != t[j - 1]:
            if table[j] == 0:
                table[j] = j - k
            j = f[j]

    k = f[0]
    for j in range(len(t) + 1):
        if table[j] == 0:
            table[j] = k
        if j == k:
            k = f[k]

    return table


def boyer_moore_search(s, t):
    bad_calacter_heuristic_table = create_bad_calacter_heuristic_table(t)
    good_suffix_heuristic_table = create_good_suffix_heuristic_table(t)
    i = 0
    res = []
    while i + len(t) <= len(s):
        j = len(t) - 1
        k = i
        while j >= 0 and s[i + j] == t[j]:
            j -= 1
        if j < 0:  # 検索パターンと一致しているため出力に追加、Bad Character Heuristicが使えないためシフト幅はGood Suffix Heuristicにより決定
            res.append(i)
            shift = good_suffix_heuristic_table[0]
        else:
            shift = max(j - bad_calacter_heuristic_table[s[i + j]], good_suffix_heuristic_table[j + 1])  # 2つの規則のうちシフト幅が大きい方を最終的なシフト幅とする
        i += shift
    return res

dp = [inf] * (len(T) + 1)
dp[0] = 0

for i in range(N):
    a, *ss = input().split()
    a = int(a)
    revise = []
    for s in ss:
        res = boyer_moore_search(T, s)
        for r in res:
            revise.append((r+len(s), r))
    revise.sort()
    for r, s in reversed(revise):
        dp[r] = min(dp[r], dp[s] + 1)
if dp[len(T)] == inf:
    print(-1)
else:
    print(dp[len(T)])
        
