import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

li = [[0 for i in range(n+1)] for _ in range(n+1)]

for _ in range(m): # 배열에 간선을 저장한다.
    x,y = map(int,sys.stdin.readline().split())
    li[x][y] = 1
    li[y][x] = 1

visit = [0 for _ in range(n+1)] # 탐색한 노드를 저장하는 배열

cnt = 0
def dfs(v): # dfs 방식으로 구현.
    global cnt
    visit[v] = 1
    for i in range(1,n+1): 
        if visit[i] == 0 and li[v][i] == 1:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)

