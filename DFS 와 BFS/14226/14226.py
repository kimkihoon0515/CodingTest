import sys
from collections import deque

s = int(sys.stdin.readline())

visit = [[-1 for i in range(s+1)] for _ in range(s+1)]

def bfs():
    queue = deque()
    queue.append([1,0])
    visit[1][0] = 0
    
    while queue:
        x,y = queue.popleft()
        
        if visit[x][x] == -1: # 이모티콘을 클립보드에 복사하는 연산
            visit[x][x] = visit[x][y] + 1 # 횟수를 하나 늘린다.
            queue.append([x,x])
        if x+y <=s and visit[x+y][y] == -1: # 복사한 이모티콘을 화면에 붙여넣기 하는 연산
            visit[x+y][y] = visit[x][y] + 1 # 횟수를 하나 늘린다.
            queue.append([x+y,y])
        if x-1 >=0 and visit[x-1][y] == -1: # 화면의 이모티콘중 하나를 지운다.
            visit[x-1][y] = visit[x][y] + 1 # 횟수를 하나 늘린다.
            queue.append([x-1,y])
bfs()
answer = visit[s][1] # s개의 이모티콘이 화면에 나오는데 걸리는 시간

for i in range(1,s):
    if visit[s][i] != -1: 
        answer = min(answer,visit[s][i]) # 그 중 최소값
print(answer)