import sys

n,m,x,y,k = map(int,sys.stdin.readline().split())

pos = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dice = [0 for i in range(6)]
move = list(map(int,sys.stdin.readline().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(k):
    direction = move[i]-1
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if 0 <= nx < n and 0 <= ny < m :
        if direction == 0:
            dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
        elif direction == 1:
            dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
        elif direction == 2:
            dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
        else:
            dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]
        
        if pos[nx][ny] == 0:
            pos[nx][ny] = dice[5]
        else:
            dice[5] = pos[nx][ny]
            pos[nx][ny] = 0
            
        x,y = nx,ny
        print(dice[0])