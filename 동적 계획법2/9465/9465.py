import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline())
    sticker = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    for i in range(1,n):
        if i == 1:
            sticker[0][i] +=sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else:
            sticker[0][i] += max(sticker[1][i-1],sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1],sticker[0][i-2])
    print(max(sticker[0][n-1],sticker[1][n-1]))