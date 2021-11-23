import sys

n,m,k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split())) # 가격

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visit = [0 for _ in range(n)] 

def dfs(x, friend): # 어떤 점에서 시작해서 친구관계가 끝나는지 판별
    visit[x] = 1
    for i in graph[x]:
        if visit[i] == 0:
            friend.append(i)
            dfs(i, friend)
    return friend # 친구관계list를 return한다.

result = []
for i in range(n):
    if visit[i] == 0 : # 탐색을 안했다면
        li = dfs(i, [i]) # 그 사람의 친구목록을 반환하고
        minimum = sys.maxsize 
        for j in li: # 그 친구목록에서 친구비의 최소값을 구한다.
            if minimum > A[j]:
                minimum = A[j]
        result.append(minimum) # 그리고 결과값에 넣는다.

if sum(result) <= k: 
    print(sum(result))
else:
    print('Oh no')