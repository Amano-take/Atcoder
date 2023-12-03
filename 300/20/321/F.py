import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
15 10
+ 5
+ 2
+ 3
- 2
+ 5
+ 10
- 3
+ 1
+ 3
+ 3
- 5
+ 1
+ 7
+ 4
- 3
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
