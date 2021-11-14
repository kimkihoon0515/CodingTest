""" deque를 통해 구하면 중복된 graph 값이 들어오면 메모리 초과가 난다.
import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())

graph = [list(map(str,input())) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    global result # 갈 수 있는 경로의 최대 수
    queue = deque()
    queue.append([x,y,graph[x][y]])

    while queue:
        a,b,ans = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ans: # 중복되는지 검사
                queue.append([nx,ny,ans+graph[nx][ny]])
                result = max(result,len(ans)) 

result = 1 
bfs(0,0)
print(result+1) # 시작점도 세기 때문에
"""
import sys
r,c = map(int,sys.stdin.readline().split())

graph = [list(map(str,input())) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    global result # 갈 수 있는 경로의 최대 수
    queue = set([(x,y,graph[x][y])])

    while queue:
        a,b,ans = queue.pop()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ans: # 중복되는지 검사
                queue.add((nx,ny,ans+graph[nx][ny]))
                result = max(result,len(ans)+1) 

result = 1 
bfs(0,0)
print(result) # 시작점도 세기 때문에