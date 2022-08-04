import sys

n = int(sys.stdin.readline())

li = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0
count = 0

def dfs(x,y):
    global cnt
    if x < 0 or x >= n or y <0 or y>=n:
        return False
    if li[x][y] ==1:
        cnt +=1
        li[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False        


for i in range(n):
    li.append(list(map(int,input())))

result = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count +=1
            result.append(cnt)
            cnt = 0
print(count)
result.sort()
for i in range(len(result)):
    print(result[i])

