from collections import deque
def solution(n, edge):
    answer = 0    
    graph = [[] for _ in range(n+1)]
    visit = [0 for i in range(n+1)]
    
    def bfs(x):
        queue = deque()
        queue.append(x)
        visit[x] = 1
        
        while queue:
            a = queue.popleft()
            for i in graph[a]:
                if visit[i] == 0:
                    visit[i] = visit[a] + 1
                    queue.append(i)
    
    for a,b in edge: # 그래프를 연결된 노드들의 구성으로 만들어놓는다.
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    bfs(1) # 시작 노드는 1이므로 1 대입
    for i in visit: # 가장 먼 거리의 노드들의 개수만 출력
        if i == max(visit):
            answer +=1
    return answer