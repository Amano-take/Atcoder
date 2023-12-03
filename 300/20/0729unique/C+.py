import sys
import io
import math
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10**8)



N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x) + 1, input().split()))
A.extend(B)
A.sort()

print(A[M-1])

#A[0] の時　売りたい人 - 買いたい人　= - M + 1 (A[0] <- seller, number of seller is 1, and number of buyer = M. A[0] <- buyer+1, number of seller is 0, and number of buyer = M-1)
#then A[i] num of seller - num of buyer = - M + (i + 1) 
#So, A[M-1] equals Answer