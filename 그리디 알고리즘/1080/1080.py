import sys

n,m = map(int,sys.stdin.readline().split())

a = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def convert(x,y): # 행렬 변환
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j] = 1 - a[i][j]


result = 0
for i in range(n-2): 
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            convert(i,j)
            result +=1

answer = 0
for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            answer = -1

if answer == -1:
    print(-1)
else:
    print(result)