import sys
import io
sys.setrecursionlimit(10**8)


def binary_serch(mid):
    edge = 0
    k = 0
    for i in range(N+1):
        if A_list[i] - edge >= mid:
            edge = A_list[i]
            k += 1
    return k >= K+1


N, L = map(int, input().split())
K = int(input().strip())
A_list = list(map(int, input().split() + [L]))

left = 0
right = L+1
while True:
    middle = (left + right) // 2
    if binary_serch(middle):
        left = middle
    else:
        right = middle
    if right == left + 1:
        print(left)
        break


