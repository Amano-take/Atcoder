import sys
inf = float('inf')

input = lambda: sys.stdin.readline().strip()
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
MOD = 10**9+7
from collections import defaultdict
from collections import deque





class segTree():
    def __init__(self, setList, func, identity=None):
        self.L = 1 << (len(setList) - 1).bit_length()
        self.func = func
        self.identity = identity
        self.binaryTree = [self.identity]*(self.L*2-1)
        self.binaryTree[self.L-1:self.L-1+len(setList):1] = setList
        self.se = [(0, 0)] * (self.L - 1)
        self.se.extend([(i, i+1) for i in range(self.L)])
        for i in range(self.L - 2, -1, -1):
            self.binaryTree[i] = self.func(self.binaryTree[2*i + 1], self.binaryTree[2*i + 2])
            self.se[i] = (self.se[2*i + 1][0] , self.se[2*i+2][1])
        
    def show(self):
        j = 1
        for i in range(self.L*2-1):
            print(self.binaryTree[i], end=" ")
            if i == 2 ** j - 2:
                j += 1
                print()
        print("------")
        j = 1
        for i in range(self.L*2-1):
            print(self.se[i], end=" ")
            if i == 2 ** j - 2:
                j += 1
                print()

    def set(self, index, value):
        """
        indexは0はじまり
        """
        
        
        index = self.L - 1 + index
        if self.binaryTree[index] <= value:
            return
        self.binaryTree[index] = value
        while True:
            index = (index - 1 ) // 2
            self.binaryTree[index] = self.func(self.binaryTree[2*index + 1], self.binaryTree[2*index + 2])
            if index == 0:
                break
    
    def query(self, start, end):
        """
        [start, end)\n
        start, end それぞれ0はじまり
        """
        return self.recquery(0, start, end)

    def recquery(self, index, start, end):
        if start >= end:
            return self.identity
        s, e = self.se[index]
        #完全に包含される場合
        if s >= start and e <= end:
            return self.binaryTree[index]
        #部分的に一致する場合
        elif start < e and end > s:
            return self.func(self.recquery(index*2+1, start, end), self.recquery(index*2+2, start, end))
        #完全に一致しない場合
        else:
            return self.identity
        
    def stack_query(self,start, end):
        stack = deque([0])
        ans = self.identity
        while len(stack) != 0:
            index = stack.pop()
            s, e = self.se[index]
            #完全に一致する場合
            if s >= start and e <= end:
                ans = self.func(ans, self.binaryTree[index])
            #部分的に一致する場合
            elif start < e and end > s:
                stack.append(index*2 + 2)
                stack.append(index*2 + 1)
            #完全に一致しない場合
            else:
                continue
        return ans

    
def solve():
    n = int(input())
    s = set()
    d = defaultdict(list)
    for _ in range(n):
        x, y, z = sorted(MII())
        d[x].append((y, z))
        s.add(y)

    mp = {x: i + 1 for i, x in enumerate(sorted(s))}
    t = segTree([inf]*(n+1), min, inf)
    for x in sorted(d.keys()):
        for y, z in d[x]:
            if t.stack_query(0, mp[y]) < z:
                return print('Yes')
        for y, z in d[x]:
            t.set(mp[y], z)
    print('No')
    return
solve()
