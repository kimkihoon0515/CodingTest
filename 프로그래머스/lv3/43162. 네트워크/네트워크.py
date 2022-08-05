from collections import deque

def solution(n, computers):
    answer = 0
    
    visit = [0 for i in range(n)]
    
    def bfs(a):
        queue = deque()
        queue.append(a)
        
        visit[a] = 1
        
        while queue:
            x = queue.popleft()
            
            for i in range(n):
                if visit[i] == 0 and computers[x][i] == 1:
                    visit[i] = 1
                    queue.append(i)
    for i in range(n):
        if visit[i] == 0:
            bfs(i)
            answer+=1
    return answer