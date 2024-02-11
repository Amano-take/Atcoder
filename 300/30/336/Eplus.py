import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

input=lambda: sys.stdin.readline().strip()

dp = [[[[[0]*128 for _ in range(128)] for _ in range(2)] for _ in range(2)] for _ in range(15)]
check = [[[[[0]*128 for _ in range(128)] for _ in range(2)] for _ in range(2)] for _ in range(15)]
cur = 0

def count(index, larger, smaller, left, mod, sum, L, R):
    if index == len(L):
        if left == 0 and mod == 0:
            return 1
        return 0
    if (len(L) - index) * 9 < left:
        return 0
    if check[index][larger][smaller][left][mod] == cur:
        return dp[index][larger][smaller][left][mod]
    check[index][larger][smaller][left][mod] = cur
    x = int(L[index])
    y = int(R[index])
    result = 0
    for i in range(10):
        if i > left:
            break
        if x > i and larger == 0:
            continue
        if y < i and smaller == 0:
            continue
        nxtLarger = larger
        nxtSmaller = smaller
        if x < i:
            nxtLarger = 1
        if y > i:
            nxtSmaller = 1
        nxtMod = (mod * 10 + i) % sum
        result += count(index + 1, nxtLarger, nxtSmaller, left - i, nxtMod, sum, L, R)
    dp[index][larger][smaller][left][mod] = result
    return result

def main():
    global cur
    r = int(input())
    L = str(1)
    R = str(r)
    while len(L) < len(R):
        L = "0" + L
    result = 0
    for j in range(1, 9*14+1):
        cur += 1
        result += count(0, 0, 0, j, 0, j, L, R)
    print(result)

if __name__ == "__main__":
    main()