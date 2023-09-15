import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
tourist
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

nl = [("tourist", 3858), ("ksun48", 3679), ("Benq", 3658), ("Um_nik",  3648), ("apiad", 3638), ("Stonefeang", 3630), ("ecnerwala", 3613), ("mnbvmar", 3555), ("newbiedmy", 3516), ("semiexp", 3481)]

s = input()
for name, rate in nl:
    if s == name:
        print(rate)
        break