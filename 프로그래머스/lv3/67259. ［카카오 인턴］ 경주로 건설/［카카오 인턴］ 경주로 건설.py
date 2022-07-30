from collections import deque
import sys

def solution(board):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(board)
    
    def bfs(start):
        cost = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append(start)
        
        cost[0][0] = 0
        while queue:
            x,y,dir,c = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if dir!=i:
                    n_cost = c+600
                else:
                    n_cost = c+100
                if 0<=nx<n and 0<=ny<n and board[nx][ny]!=1:
                    if cost[nx][ny]>n_cost:
                        cost[nx][ny] = n_cost
                        queue.append([nx,ny,i,n_cost])
        return cost[-1][-1]
    answer = (min(bfs((0,0,1,0)),bfs((0,0,3,0))))
    return answer