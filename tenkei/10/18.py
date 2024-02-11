import sys
import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    e = int(input())
    ang = e * math.pi * 2 / T
    y = 2 / L + math.sin(-ang  + )