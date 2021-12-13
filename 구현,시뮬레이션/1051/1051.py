import sys

n,m = map(int,sys.stdin.readline().split()) 

li = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

answer = 0

for i in range(n): # 세로
    for j in range(m): # 가로
        for k in range(min(n,m)): # 정사각형의 한 변의 길이
            if i+k < n and j+k <m and li[i][j] == li[i][j+k] == li[i+k][j+k] == li[i+k][j]: # 범위를 넘지 않고 모든 점이 같다면
                answer = max(answer,(k+1)**2)

print(answer)
            