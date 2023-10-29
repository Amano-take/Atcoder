import sys
import io
import itertools
import copy

sys.setrecursionlimit(10**8)
_INPUT = """\
5
ABCBC
ACAAB
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
R = list(input())
C = list(input())
choice = list("ABC")
for _ in range(N-3):
    choice.append(".")

def start(s):
    for ss in s:
        if ss == ".":
            continue
        else:
            return ss
    return "."

def dfs(row:list, col, r):
    for i in range(N):
        if start(col[i]) not in [".", C[i]]:
            return False, row
    
    if r != N:
        for gyou in itertools.permutations(choice):
            if start(gyou) != R[r]:
                continue
            
            row[r] = gyou
            for i in range(N):
                col[i][r] = gyou[i]
            b, row = dfs(row, col, r+1)
            if b:
                return b, row
            else:
                row[r] = ["."] * N
                for i in range(N):
                    col[i][r] = "."
        return False, row
    else:
        for i in range(N):
            s = "".join(sorted(col[i]))
            s = s.replace(".", "")
            if s != "ABC":
                break
            if start(col[i]) != C[i]:
                break
        else:
            return True, row
        
        return False, row
        
b, row = dfs([["."] * N for _ in range(N)], [["."]* N for _ in range(N)], 0)
if b:
    print("Yes")
    for i in range(N):
        print("".join(row[i]))
else:
    print("No")
            
                
