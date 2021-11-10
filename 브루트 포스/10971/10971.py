import sys

n = int(sys.stdin.readline())

li = []

min_cost = sys.maxsize

for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

def dfs(start,finish,money,visited):
    global min_cost

    if len(visited) == n:
        if li[finish][start] != 0: # 갈 수 있으면
            min_cost = min(min_cost,money+li[finish][start]) # 최소비용을 갱신한다.
        return
    for i in range(n):
        if li[finish][i] != 0 and i not in visited and money < min_cost: # 다음 도시로 갈 수 있고 아직 방문하지 않았고 그 도시로 가는 비용이 최소비용보다 작을 경우
            visited.append(i) # 방문목록에 추가하고
            dfs(start,i,money+li[finish][i],visited) # 그 상태에서 다시 돌린다.
            visited.pop() # 방문목록에서 제거

visited = [i for i in range(n)]
for i in range(n):
    dfs(i,i,0,visited[i])
print(min_cost)
