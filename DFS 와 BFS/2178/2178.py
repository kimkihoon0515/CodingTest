import sys

n,m = map(int,sys.stdin.readline().split())

li = []
"""
101111
101010
101011
111011
"""
for _ in range(n):
    li.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

queue = [[0,0]]
while(queue): # bfs 방식으로 탐색하는 법
    a,b = queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1:
            queue.append([nx,ny])
            li[nx][ny] = li[a][b] + 1 # 1을 발견할때마다 하나씩 늘어나서 마지막까지 탐색한다. 

print(li[n-1][m-1])




