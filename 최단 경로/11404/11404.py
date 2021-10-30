# floyd warshall 알고리즘을 사용한다.
"""
그래프에서 모든 꼭짓점 사이의 최단 경로의 거리를 구하는 알고리즘이다. 
음수 가중치를 갖는 간선도 순환만 없다면 잘 처리된다. 
제일 바깥쪽 반복문은 거쳐가는 꼭짓점이고, 두 번째 반복문은 출발하는 꼭짓점, 세 번째 반복문은 도착하는 꼭짓점이다. 
이 알고리즘은 플로이드 알고리즘이라고도 알려져 있다.
선행 조건으로는 2차원 배열 d에는 두 정점 간의 비용이 초기화 되어 있어야한다.
두 정점 간의 연결이 없다면 무한대로 초기화한다.
무한대로 초기화하는 이유는 이 무한대를 이용하여 두 정점간의 연결 여부를 파악하기 위해서다.
d 배열의 값이 무한대가 아니면 두 정점이 연결되어 있다는 의미이다.
"""
import sys

inf = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(c,graph[a][b]) # 입력값보다 짧은 경로가있으면 

for k in range(1,n+1): # floyd warshall 알고리즘이다.
    for j in range(1,n+1): 
        for i in range(1,n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0,end=' ') # 경로가없을 경우
        else:
            print(graph[i][j],end=' ')
    print()