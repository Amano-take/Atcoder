import sys
import io
import numpy as np
sys.setrecursionlimit(10**8)

def main():
    global array, N, M
    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    for i, l in enumerate(readlines()):
        if i==0:
            N, M = map(int, l.split())
            tmp = [[] for i in range(N)]
        else:
            tmp[i-1] = list(map(lambda i: i=='.', l.strip()))
    array = np.array(tmp)
    can_go=set(((1,1),))
    can_stop = set()
    dfs((1,1), can_go, can_stop)
    print(len(can_go))

def dfs(stop, can_go, can_stop):
    global array, N, M
    #top
    for i in range(N):
        if array[stop[0]+i][stop[1]]:
            can_go.add((stop[0]+i, stop[1]))
        else:
            if (stop[0]+i-1, stop[1]) in can_stop:
                break
            can_stop.add((stop[0]+i-1, stop[1]))
            dfs(((stop[0]+(i-1), stop[1])), can_go, can_stop)
            break

    for i in range(N):
        if array[stop[0]-i][stop[1]]:
            can_go.add((stop[0]-i, stop[1]))
        else:
            if (stop[0]-i+1, stop[1]) in can_stop:
                break
            can_stop.add((stop[0]-i+1, stop[1]))
            dfs(((stop[0]-(i-1), stop[1])), can_go, can_stop)
            break

    for i in range(M):
        if array[stop[0]][stop[1]+i]:
            can_go.add((stop[0], stop[1]+i))
        else:
            if (stop[0], stop[1]+(i-1)) in can_stop:
                break
            can_stop.add((stop[0], stop[1]+i-1))
            dfs(((stop[0], stop[1]+i-1)), can_go, can_stop)
            break
    
    for i in range(M):
        if array[stop[0]][stop[1]-i]:
            can_go.add((stop[0], stop[1]-i))
        else:
            if (stop[0], stop[1]-i+1) in can_stop:
                break
            can_stop.add((stop[0], stop[1]-i+1))
            dfs(((stop[0], stop[1]-i+1)), can_go, can_stop)
            break
            

if __name__ == "__main__":
    main()