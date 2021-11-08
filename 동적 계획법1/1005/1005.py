import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n,k = map(int,sys.stdin.readline().split()) # 건물의 개수 n, 건물간의 건설 순서 규칙의 총 개수 k
    li = list(map(int,sys.stdin.readline().split())) # 각 건물당 걸리는 시간
    degree = [0] * (n+1) # 위상정렬을 사용하기 위한 차수 배열
    dp = [0] *(n+1) # 걸리는 시간
    cost = [[] for _ in range(n+1)] # 건설 순서
    
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split()) # 건설순서 x를 지은 다음 y를 지을 수 있다.
        cost[x].append(y) # 건설순서 저장
        degree[y] +=1 # 진입 차수를 1증가

    w = int(sys.stdin.readline()) # 승리하기 위해 건설해야 하는 건물의 번호

    queue = deque() 

    for i in range(1,n+1): # 처음 진입할 때는 진입차수가 0인 노드를 큐에 넣고 
        if degree[i] == 0:
            queue.append(i)
            dp[i] = li[i-1] # 걸리는 시간도 넣는다.
    
    while queue: # queue 가 빌 때까지 반복한다.
        a = queue.popleft()

        for i in cost[a]:
            degree[i] -= 1 # 진입차수를 줄이고 비용을 갱신함.
            dp[i] = max(dp[i],dp[a]+li[i-1]) # dp를 이용해서 비용 갱신
            if degree[i] == 0:
                queue.append(i)
    print(dp[w])

