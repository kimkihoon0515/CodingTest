import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
"""
1 2 1 3 1 2 1
앞 뒤가 똑같은 수
(1,3) (3,5) (5,7) 
"""

m = int(sys.stdin.readline())
dp = [[0 for _ in range(n)]for _ in range(n)]


for i in range(n): # 사이 간격이 1일때 
    dp[i][i] = 1

for i in range(n-1): # 사이 간격이 2일때 
    if li[i] == li[i+1]:
        dp[i][i+1] = 1

for i in range(2,n): # 사이 간격이 3이상일 때
    for j in range(n-i): 
        if li[j] == li[j+i] and dp[j+1][i+j-1] == 1: # 처음과 끝이 같고 중간과정이 팰린드롬이면 그 간격도 팰린드롬이다.
            dp[j][i+j] = 1

for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])
