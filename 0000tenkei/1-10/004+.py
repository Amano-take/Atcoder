H, W = map(int, input().split())
A = [list(map(int, input()).split()) for _ in range(H)]

yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))

