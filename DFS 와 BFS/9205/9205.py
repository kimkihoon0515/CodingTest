import sys

t = int(sys.stdin.readline())

inf = sys.maxsize

for i in range(t):
    n = int(sys.stdin.readline()) # 맥주를 파는 편의점의 수
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n+2)] # 집, 편의점, 락 페스티벌 좌표
    visit = [[inf for i in range(n+2)] for i in range(n+2)] # 거리 

    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue
            distance = abs(graph[i][0]-graph[j][0]) + abs(graph[i][1]-graph[j][1]) # 각 좌표들의 거리
            if distance <= 1000: # 1000 이하면 방문
                visit[i][j] = 1

    for k in range(n+2): # floyd warshall 알고리즘
        for a in range(n+2):
            for b in range(n+2):
                if visit[a][b] > visit[a][k] + visit[k][b]:
                    visit[a][b] = visit[a][k] + visit[k][b]

    if 0 <= visit[0][n+1] < inf: # 시작부터 락 페스티벌에 가는 길이가 천 이하이면 happy를 아니면 sad를 출력
        print('happy')
    else:
        print('sad')