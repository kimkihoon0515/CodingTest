import sys

graph = [list(map(str,sys.stdin.readline().split())) for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []

def dfs(i,j,num):
    if len(num) > 5:
        if num not in result:
            result.append(num)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,num+graph[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
print(len(result))