import sys
import io
import math
sys.setrecursionlimit(10**8)


N, M = map(int, input().split())
S = [input() for _ in range(N)]
for i in range(0, N-9+1):
    for j in range(0, M-9+1):
        flag = True
        for n in range(0, 3):
            if S[i+n][j:j+4] != "###.":
                flag = False
            if S[i+8-n][j+5:j+9] != ".###":
                flag = False
        flag = flag and S[i+3][j:j+4] == "...."
        flag = flag and S[i+5][j+5:j+9] == "...."
        if flag:
            print(*[i+1, j+1])