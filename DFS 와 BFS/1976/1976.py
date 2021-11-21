import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

tour = list(map(int,sys.stdin.readline().split())) # 여행 계획 (1,2,3)

for k in range(n): # floyd warshall 로 모든 경로를 계산한다.
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 1 # 자기 자신을 1로 만들고
            if graph[a][k] == 1 and graph[k][b] == 1: # 거쳐서 갈 수 있는경우 1로 만든다.
                graph[a][b] = 1

for i in range(1,len(tour)):
    if graph[tour[i-1]-1][tour[i]-1] != 1: # 여행 계획의 경로를 graph에서 탐색해서 경로가 1이면 yes를 아니면 no를 출력한다.
        print('NO')
        exit(0)

print('YES')