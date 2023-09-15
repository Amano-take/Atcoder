import sys
import io
import numpy as np

def main():

    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    for i, l in enumerate(readlines()):
        if i==0:
            N, D = map(int, l.split())
            cul = np.zeros((N, D))
        else:
            cul[i-1] = list(map(lambda i: i=='o', l.strip()))

    TF = np.all(cul==1, axis=0)
    j = 0
    max = 0
    for i in TF:
        if i:
            j += 1
        else:
            j = 0
        if j > max:
            max = j
    print(max)

if __name__ == "__main__":
    main()