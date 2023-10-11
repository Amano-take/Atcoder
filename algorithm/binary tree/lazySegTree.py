import math


class lasySegTree():
    def __init__(self, setList, func, identity=None):
        self.L = 2 ** math.ceil(math.log2(len(setList)))
        self.func = func
        self.identity = identity
        self.lazy = []

        while len(setList) != self.L:
            setList.append(identity)
        self.binaryTree = [0] * (self.L - 1)
        self.binaryTree.extend(setList)
        self.se = [0] * (self.L - 1)
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
        print(index, start, end)
        if start == end:
            return self.identity
        s, e = self.se[index]
        #完全に一致する場合
        if s == start and e == end:
            return self.binaryTree[index]
        #部分的に一致する場合
        elif s <= start and e >= end:
            mid = self.se[index*2+1][1]
            return self.func(self.recquery(index*2+1, start, mid), self.recquery(index*2+2, mid, end))
        #完全に一致しない場合
        elif s > start or e < end:
            return self.identity