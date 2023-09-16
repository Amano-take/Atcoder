class unionfind():
  def __init__(self, n):
    self.n=n
    self.parents=[-1]*n
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]
  def unit(self, x, y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    else:
      if self.size(x)<self.size(y):
        x,y=y,x
      self.parents[x]+=self.parents[y]
      self.parents[y]=x
  def size(self,x):
    return -self.parents[self.find(x)]
  def print(self):
    print(self.parents)

import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
5 5
42
2 3 4 3 4
2 3 2 3 2
1 4 1
2 4 1 2 2
1 1 2
1 4 5
1 3 3
2 4 2 1 3
1 3 5
2 2 4 2 3
2 2 4 2 5
2 3 4 5 1
2 3 1 2 2
2 3 1 1 2
2 2 4 5 2
2 3 2 5 3
1 4 3
2 3 3 3 5
2 3 1 3 2
1 1 5
2 4 4 5 3
1 1 4
2 1 3 2 5
2 4 3 1 4
2 2 3 3 3
1 2 1
1 2 5
2 1 4 5 3
2 4 4 2 5
2 4 2 2 4
1 2 2
2 4 1 5 2
1 2 4
2 3 1 4 1
1 4 4
2 3 2 2 1
2 1 1 5 2
1 4 2
2 4 2 3 5
1 3 2
1 3 4
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
Q = int(input())
uf = unionfind(H*W)
red = [0] * (H*W)
readlines = sys.stdin.readlines()
for r in readlines:

  t, *L = map(int, r.split())
  if t==1:
    py, px = L
    node = (py-1) * W + (px-1)
    red[node] = 1
    if px != 1 and red[node - 1] == 1:
      uf.unit(node, node-1)
    if px != W and red[node + 1] == 1:
      uf.unit(node, (py-1)*W+(px))
    if py != 1 and red[node - W] == 1:
      uf.unit(node, (py-2)*W+(px-1))
    if py != H and red[node + W] == 1:
      uf.unit(node, py*W +(px-1))
  else:
    py, px, qy, qx = L
    node1 = (py-1)*W + (px-1)
    node2 = (qy-1)*W + (qx-1)
    if red[node1] * red[node2] == 1:
      if uf.find(node1) == uf.find(node2):
        print("Yes")
        continue
    print("No")



