import sys
import io

def main():
    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    data = set()
    variance = 0
    for i, l in enumerate(readlines()):
        if i == 0:
            continue
        else:
            l = l.rstrip('\n')
            if l == reverse(l) and not (l in data):
                variance += 1
            data.add(l)
            data.add(reverse(l))
    print ((len(data) + variance) // 2)


def reverse(s:str):
    res = ''
    for x in s:
        res = x + res
    return res




if __name__ == "__main__":
    main()