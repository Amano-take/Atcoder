import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
16
152 153 154 147 148 149 158 159 160 155 156 157 144 145 146 150
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
AL = list(map(int, input().split()))
AL.sort()
a = AL[0]
for i in range(len(AL)):
    if AL[i] != a + i:
        print(a + i)
        break
