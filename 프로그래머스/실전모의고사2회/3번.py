from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n+1)]

    for i in range(len(roads)):
        a,b = roads[i]
        graph[a].append(b)
        graph[b].append(a)
    

    visit = [-1 for i in range(n+1)]

    def bfs(start):
        queue = deque()
        queue.append(start)

        
        visit[start] = 0


        while queue:
            x = queue.popleft()

            for i in graph[x]:
                if visit[i] == -1:
                    queue.append(i)
                    visit[i] = visit[x]+1
        
        return visit[destination] 

    bfs(destination)


    for i in sources:
        answer.append(visit[i])

    return answer