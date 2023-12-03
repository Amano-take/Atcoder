import sys
import io
import numpy as np
sys.setrecursionlimit(10**8)

def main():

    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    for i, l in enumerate(readlines()):
        if i==0:
            N = int(l)
            remain = set(i+1 for i in range(N))
        else:
            array = np.array(list(map(int, l.split())))

    while True:
        i = 0
        v = remain.pop()
        history = set([v])
        history_list = [v]
        while True:
            v = array[v-1]
            if v in history:
                index = history_list.index(v)
                print(len(history_list) - index)
                print(*history_list[index:])
                return
            history.add(v)
            history_list.append(v)



if __name__ == "__main__":
    main()