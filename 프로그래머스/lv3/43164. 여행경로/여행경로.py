from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start,end in sorted(tickets):
        graph[start].append(end)
    
    visit = []
    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        visit.append(start)
    dfs('ICN')
    return visit[::-1]