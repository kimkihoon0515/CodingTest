import sys
# 크루스칼 알고리즘을 활용하여 푸는 문제

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x]) # 부모노드를 확인
    return parent[x]

def union(x,y):
    x,y = find(x),find(y)
    parent[x] = y

graph = []
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph.append([a,b,c])

graph = sorted(graph, key=lambda x:x[2]) # weight 기준으로 edge들을 정렬
parent = [i for i in range(0,n+2)]

ans = 0
for i in graph:
    start,end,weight = i
    if find(start) == find(end): # root 가 같게 되면 loop가 생기게 되므로 넘어간다.
        continue
    else:
        ans += weight
        union(start,end) # root가 다르면 union을 해준다.
        
print(ans)