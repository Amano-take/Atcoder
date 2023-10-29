import sys
import io
import numpy as np


def edge(point, r):
    ans = set()
    for i in range(r+1):
        ans.add((point[0]+r, point[1]+i))
        ans.add((point[0]+i, point[1]+r))
    return ans

_INPUT = """\
2 3 1
2 3
"""
sys.stdin = io.StringIO(_INPUT)
H, W, N = map(int, input().split())
hole = set([tuple(map(lambda t: int(t)-1, tuple(input().split()))) for _ in range(N)])
array = np.zeros((H, W))
for sum in range(H+W-1):
    for i in range(max(0,sum-W+1), min(sum+1, H)):
        if i == 0:
            start_index = int(array[i][sum-i-1])-1
        elif sum - i == 0:
            start_index = int(array[i-1][sum-i])-1
        else:
            start_index = int(max(array[i-1][sum-i], array[i][sum-i-1]))-1
        for r in range(start_index-1, min(H-i, W-sum+i)):
            if len(edge((i, sum-i), r) & hole) != 0:
                array[i][sum-i] = r
                break
            else:
                array[i][sum-i] = r+1
print(int(np.sum(array)))
