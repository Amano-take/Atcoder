import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

input=lambda: sys.stdin.readline().strip()
T  = int(input())
    

def solve():
    N = int(input())
    if N == -1:
        exit()
    left = 1
    right = N
    if N == 1:
        print("? 1")
        sys.stdout.flush()
        a = int(input())
        print(f"! {a}")
        sys.stdout.flush()
        return
    dic = ddict(int)
    while left < right:
        mid = (left + right) // 2
        q1 = mid
        q2 = mid + 1
        if q1 in dic:
            a1 = dic[q1]
        else:
            print(f"? {q1}")
            sys.stdout.flush()
            a1 = int(input())
            dic[q1] = a1
        if q2 in dic:
            a2 = dic[q2]
        else:
            print(f"? {q2}")
            sys.stdout.flush()
            a2 = int(input())
            dic[q2] = a2
        if left == right - 1 and a1 < a2:
            print(f"! {dic[right]}")
            sys.stdout.flush()
            return
        elif left == right - 1 and a1 > a2:
            print(f"! {dic[left]}")
            sys.stdout.flush()
            return
        if a1 < a2:
            left = q2
        else:
            right = q1
    print(f"! {dic[left]}")
    sys.stdout.flush()
        
for _ in range(T):
    solve()
