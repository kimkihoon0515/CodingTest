import sys
#sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
result = [] # 결과 배열

def dfs(s,i): # 시작점과 인덱스
    visit[s] = 1 # 시작주소를 방문했으므로
    for node in graph[s]: # dfs 탐색
        if visit[node] == 0:
            dfs(node,i) 
        elif visit[node] == 1 and node == i: # 방문했고 node가 이전에 방문했던 지점과 같으면
          result.append(node)  # 결과배열에 넣는다.


for i in range(1,n+1):
    a = int(sys.stdin.readline().strip())
    graph[i].append(a)
    
for i in range(1,n+1):
    visit = [0 for i in range(n+1)]
    dfs(i,i)

print(len(result))
result = sorted(result)
for i in result:
    print(i)
