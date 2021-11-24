from collections import deque

graph = [list(map(str,input())) for _ in range(12)]

def down(): # 내리기 함수
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if graph[j][i] != '.' and graph[k][i] == '.': 
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[0 for _ in range(6)] for _ in range(12)]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    change.append([x,y]) # 시작지점 글자와 같은 글자위치만 넣을 배열 

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0:
                if graph[nx][ny] == graph[x][y]:
                    visit[nx][ny] = 1
                    queue.append([nx,ny])
                    change.append([nx,ny])

ans = 0
while True:
    flag = False
    visit = [[0 for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if visit[i][j] == 0 and graph[i][j] != '.':  # 탐색지점 
                visit[i][j] = 1
                change = []
                bfs(i,j)
                if len(change) > 3: # 같은 글자가 4개이상 나오면
                    flag = True
                    for x,y in change:
                        graph[x][y] = '.' # 그 구간을 전부 .으로 바꿔준다.
    if flag == False: # 만약 연쇄작용이 일어나는 곳이 더 이상 없으면 종료
        break
    down() #연쇄작용이 한번 일어나면 그 구간을 전부 내리는 down 실행
    ans += 1 # 연쇄작용 1 추가
print(ans)