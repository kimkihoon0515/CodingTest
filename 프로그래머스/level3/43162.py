from collections import deque
def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)] # 방문 배열
    def bfs(x):
        queue = deque()
        queue.append(x)
        visit[x] = 1
        while queue:
            a = queue.popleft()
            for i in range(n):
                if visit[i]==0 and computers[a][i] == 1: # 방문을 안했고 컴퓨터와 연결되어있다면
                    visit[i] = 1 # 방문 한것으로 갱신
                    queue.append(i) # 큐에 넣기
                    
    for i in range(n):
        if visit[i] == 0: # 아직 방문안했다면
            bfs(i) # bfs 돌리고
            answer +=1 # 네트워크 개수 1증가
    return answer