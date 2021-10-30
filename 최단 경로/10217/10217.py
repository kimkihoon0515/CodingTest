import sys
 
t=int(input())
inf=sys.maxsize
 
for _ in range(t):
    n,m,k=map(int,sys.stdin.readline().split()) # 공항수,지원비용,티켓정보수
    graph=[[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d=map(int,sys.stdin.readline().split()) # 출발,도착,비용,소요시간
        graph[u].append([v,c,d])
 
 
    dp=[[inf for _ in range(m+1)] for _ in range(n+1)] # 열:비용 행:n까지갈때
    dp[1][0]=0 # 1->1로 갔을때 비용은0 시간도 0
 
    for c in range(m+1):
        for d in range(1,n+1):
            if dp[d][c]==inf:
                continue # c의 비용으로 d에 도착하는 경우가 없다면
            t=dp[d][c] # c의 비용으로 d에 도착햇을때의 소요시간
            for dv,dc,dd in graph[d]: # d에서 출발하는 모든경우
                if dc+c>m: # 비용이 초과될경우 넘어간다
                    continue
                dp[dv][dc+c]=min(dp[dv][dc+c],t+dd) # 이전에 저장된값과 비교하여 작다면 갱신해준다
 
    result=min(dp[n]) # n에 도착할때 최소소요시간
 
    if result==inf:
        print('Poor KCM')
    else:
        print(result)
