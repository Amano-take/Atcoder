import abc

class Tree(abc.ABC):
    @property
    @abc.abstractmethod
    def insert(self, value):
        pass

    @property
    @abc.abstractmethod
    def print(self):
        pass

class Root(Tree):
    def __init__(self):
        self.Node = None
        pass

    def insert(self, value):
        if self.Node == None:
            self.Node = Node(value, None, None)
        else:
            self.Node.insert(value)
        return self.Node
    
    def print(self):
        self.Node.print()
        return
    
    def searchclose(self, value):
        return self.Node.searchclose(value)

class Leaf(Tree):
    def __init__(self, value):
        self.v = value
        self.l = None
        self.r = None
    
    def insert(self, value):
        if value < self.v:
            return Node(self.v, Leaf(value), None)
        else:
            return Node(self.v, None, Leaf(value))
        
    def print(self):
        print(str(self.v), end=" ")

    def searchclose(self, value):
        return self.v

class Node(Tree):
    def __init__(self, value, left, right):
        self.v = value
        self.l = left
        self.r = right

    def insert(self, value):
        if value < self.v:
            if self.l != None:
                self.l = self.l.insert(value)
            else:
                self.l = Leaf(value)
        else:
            if self.r != None:
                self.r = self.r.insert(value)
            else:
                self.r = Leaf(value)
        return self
    
    def print(self):
        if self.l != None:
            self.l.print()
        print(str(self.v), end=" ")
        if self.r != None:
            self.r.print()

    def searchclose(self, value):
        if self.v == value:
            return self.v
        elif value < self.v:
            if self.l == None:
                return self.v
            a = self.l.searchclose(value)
            if abs(a - value) <= self.v - value:
                return a
            else:
                return self.v
        elif value > self.v:
            if self.r == None:
                return self.v
            a = self.r.searchclose(value)
            if abs(a - value) <= value - self.v:
                return a
            else:
                return self.v
            
import sys
import io

N = int(input())
t = Root()
for A in map(int, input().split()):
    t.insert(A)
Q = int(input())
for i in range(Q):
    b = int(input())    
    cl = t.searchclose(b)
    print(abs(b - cl))