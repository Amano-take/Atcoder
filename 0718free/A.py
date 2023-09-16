import sys
import io


def main():
    _INPUT = """\
5 6
10000 2 1 3
15000 3 1 2 4
30000 3 1 3 5
35000 2 1 5
100000 6 1 2 3 4 5 6
"""
    sys.stdin = io.StringIO(_INPUT)
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N = 0
    min_price = 0
    for i, l in enumerate(readlines()):
        if i == 1:
            N, P, Q = map(int, l.split())
            min_price = P
        else:
            for price in l.split():
                if price + Q < min_price:
                    min_price = price + Q
    
    print(min_price)


    

if __name__ == "__main__":
    print("ccc")
    main()
