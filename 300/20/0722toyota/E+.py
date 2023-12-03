H, W, N = map(int, input().split())
hole = set([tuple(map(lambda t: int(t)-1, tuple(input().split()))) for _ in range(N)])
array = [[0] * (W+1) for _ in range(H+1)]
ans = 0

for sum in range(0, H+W-1):
    for i in range(max(0, sum-(W-1)), min(H-1, sum)+1):
        if (H-i-1, W-sum+i-1) not in hole:
            array[H-i-1][W-sum+i-1] = min(array[H-i][W-sum+i-1], array[H-i-1][W-sum+i], array[H-i][W-sum+i]) +1
            ans += array[H-i-1][W-sum+i-1]
        else:
            array[H-i-1][W-sum+i-1] = 0
print(ans)