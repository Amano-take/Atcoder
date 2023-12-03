import sys
sys.setrecursionlimit(10**8)

ans = 0
N, T, M = map(int, input().split())
hate_list = set()
for i in range(M):
    A, B = map(int, input().split())
    hate_list.add((A, B))
    hate_list.add((B, A))

def count(set_list, playerA):
    
    global ans
    if T - len(set_list) > N - playerA + 1:
        return 
    elif T - len(set_list) == N - playerA + 1:
        ans += 1
        return
    elif len(set_list) > T:
        pass
    if playerA == N + 1:
        if len(set_list) == T:
            ans += 1
            return 
        else:
            return 
    else:
        set_list.append([playerA])
        count(set_list, playerA+1)
        set_list.pop()

        for set in set_list:
            if all([(playerA, p) not in hate_list for p in set]):
                set.append(playerA)
                count(set_list, playerA+1)
                set.pop()


count([], 1)
print(ans)
