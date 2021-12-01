import sys

n = int(sys.stdin.readline())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

inf = sys.maxsize

for color in range(3): # 색을 고르는 가지수
    dp = [[0 for _ in range(n)] for _ in range(3)] # i번째 집이 색을 고르면 나머지 집은 무한대로 dp를 초기화 해주기 위한 배열
    for i in range(3): # 첫 번째 집이 고른 것 외에 나머지 전부 inf 로 초기화
        if i == color:
            dp[i][0] = li[0][i]
        else:
            dp[i][0] = inf
    #print(dp)
    
    for i in range(1,len(li)): # 가격의 최소값
        dp[0][i] = min(dp[1][i-1],dp[2][i-1]) + li[i][0]
        dp[1][i] = min(dp[0][i-1],dp[2][i-1]) + li[i][1]
        dp[2][i] = min(dp[0][i-1],dp[1][i-1]) + li[i][2]
    
    for i in range(3): # 색을 다르게 정했다면
        if i != color: 
            inf = min(inf,dp[i][-1]) # R,G,B 를 골랐을 때의 최소값들을 갱신해준다.


print(inf)