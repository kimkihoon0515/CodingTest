import sys
N, K= map(int,sys.stdin.readline().split(' '))
arr = [list(map(int,sys.stdin.readline().split(' '))) for i in range(N)]
DP= [[0 for i in range(K+1)] for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if j < arr[i-1][0]:
            DP[i][j]=DP[i-1][j]
        else:
            DP[i][j]=max(DP[i-1][j],DP[i-1][j-arr[i-1][0]]+arr[i-1][1])
print(DP[N][K])
