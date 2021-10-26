import sys

n,m,v = map(int,sys.stdin.readline().split())
li = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for i in range(n+1)]

def dfs(v): # dfs는 재귀함수로 구성한다.
    print(v,end =' ')
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i] == 0 and li[v][i] == 1: # 방문하지 않았거나 간선이 연결되어있으면 다시 DFS를 돌린다.
            dfs(i)

def bfs(v): # bfs는 큐에 저장하고 반복을 돌면서 찾는 방식으로 구성한다.
    queue = [v] 
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v,end=' ')
        del queue[0]
        for i in range(1,n+1):
            if visit[i] == 1 and li[v][i] == 1: # 방문을 했고 간선이 연결되어있으면 queue에 넣어준다.
                queue.append(i)
                visit[i] = 0

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    li[x][y] = 1 # 간선이 연결되어있으면 1로 표시
    li[y][x] = 1 # 뒤집어서도 연결되어있으므로 1로 표시

dfs(v)
print()
bfs(v)