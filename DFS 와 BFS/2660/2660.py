import sys

n = int(sys.stdin.readline())

inf = sys.maxsize

graph = [[ inf for _ in range(n)] for _ in range(n)]

while True:
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    if a == -1 and b == -1:
        break

for i in range(n): # 자기 자신으로 가는 것은 0으로 초기화 해줘야한다.
    graph[i][i] = 0


for k in range(n): # floyd warshall 알고리즘으로 최단 거리 계산
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b]) 

score = 0 # 점수

result = []

for i in range(n):
    score = max(graph[i]) # 각 번호별 점수의 최대값을 result 배열에 본인의 번호와 함께 넣는다.
    result.append((i+1,score))

#print(result)
chairman = []

for i in range(n): # 회장을 뽑기 위해 번호들 중 점수의 최소값을 저장.
    score = min(score,result[i][1])

for i in range(n): # 회장후보들 저장
    if score == result[i][1]:
        chairman.append(result[i][0]) 

print(score,len(chairman))
chairman.sort()

print(*chairman)


