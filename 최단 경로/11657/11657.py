# bellman ford로 푸는 문제이다.
# queue에 넣고 최소 가중치를 찾는 것이 아니라 모든 정점에 연결되어 있는 것들을 n-1번 반복
# n-1 때도 update가 된다면 음의 가중치가 있는 것이다.
import sys, collections

inf = sys.maxsize 

graph = collections.defaultdict(list) 

n, m = map(int, sys.stdin.readline().split()) 

for _ in range(m): 
    a, b, k = map(int, sys.stdin.readline().split()) 
    graph[a].append([b, k])

def bellman_ford(s): 
    dist = [inf] * (n+1) # 시작점에서 각 정점에 걸리는 시간을 저장하는 배열
    dist[s] = 0 # 첫 시작점은 0 이므로
    for _ in range(n-1): 
        for i in range(1, n+1): 
            for j, k in graph[i]: 
                if dist[j] > dist[i] + k: # 간선 1부터 계속 걸리는 시간을 update해준다.
                    dist[j] = dist[i] + k 
    for i in range(1, n+1): 
        for j, k in graph[i]: 
            if dist[j] > dist[i] + k: 
                return False 
    return dist 

dist = bellman_ford(1) 

if dist == False: 
    print(-1) 
else: 
    for i in range(2, n+1): 
        print(dist[i] if dist[i] < inf else -1)

