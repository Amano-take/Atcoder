import sys
import io

_INPUT = """\
4 3
aaa
aaa
abc
abd
"""
sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline


H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
A = 26

row = [[0] * A for _ in range(H)]
row_c = [0] * H
col = [[0] * A for _ in range(W)]
col_c = [0] * W

num_row, num_col = H, W

for i in range(H):
    for j in range(W):
        v=ord(c[i][j]) - ord('a')
        row[i][v] += 1
        if row[i][v] == 1:
            row_c[i] += 1
        col[j][v] += 1
        if col[j][v] ==1:
            col_c[j] += 1

#row[h][v] : h行のvの色の数
#row_c[h] : h行の色の種類

while True:
    del_row, del_col = [], []
    for i in range(H):
        if row_c[i] == 1 and num_col >= 2:
            del_row.append(i)
    for j in range(W):
        if col_c[j] == 1 and num_row >= 2:
            del_col.append(j)
    if del_row == [] and del_col == []:
        break

    def remove(i, j):
        if c[i][j] != " ":
            v = ord(c[i][j]) - ord('a')
            row[i][v] -=1
            if row[i][v] == 0:
                row_c[i] -= 1
            col[j][v] -= 1
            if col[j][v] == 0:
                col_c[j] -= 1
            c[i][j] = ' '
    for i in del_row:
        for j in range(W):
            remove(i, j)
        num_row -= 1

    for j in del_col:
        for i in range(H):
            remove(i, j)
        num_col -= 1

print(num_row * num_col)