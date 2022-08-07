from collections import deque,defaultdict

def solution(n, wires):
    answer = 100000

    for i in range(len(wires)):
        graph = defaultdict(list)
        wire = wires[0:i]+wires[i+1:]
        visit = [0 for i in range(n+1)]
        for x,y in wire:
            graph[x].append(y)
            graph[y].append(x)
        def bfs(a):
            cnt = 1
            visit[a] = 1
            queue = deque()
            queue.append(a)
            
            while queue:
                x = queue.popleft()
                for node in graph[x]:

                    if visit[node] == 0:
                        visit[node] = 1
                        queue.append(node)
                        cnt+=1
            return cnt
        ans = []
        for j in range(1,n+1):
            if visit[j] == 0:
                ans.append(bfs(j))
                
        answer = min(answer,abs(ans[0]-ans[1]))

    return answer