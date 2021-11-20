import sys

n,east,west,south,north = map(int,sys.stdin.readline().split())

visit = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)] # 로봇이 방문할 수 있는 최대 공간
visit[n][n] = 1 # 

percent = [east / 100, west / 100, south / 100, north / 100] # 동 서 남 북 확률

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0

def dfs(x,y,cnt,p):
    global ans # 확률의 합

    if cnt == n:
        ans += p
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < (2*n + 1) and 0 <= ny < (2*n+1) and visit[nx][ny]: # 범위 안에 있고 방문했다면 더 이상 생각 x
            continue
        visit[nx][ny] = 1 # 방문안했으므로 했다고 하고
        dfs(nx,ny,cnt+1,p * percent[i]) # 다시 재귀함수로 돌려준다. 
        visit[nx][ny] = 0 # 현재 방문 지점을 0으로 돌려놓아야 함수가 리턴되서 튕겨져 나올 때 제대로 탐색 가능

dfs(n,n,0,1)

print(ans)