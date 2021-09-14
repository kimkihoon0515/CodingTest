import sys
N = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split(' ')))
DP= [0 for i in range(N)]
if N ==1:
    print(1)
else:
    for i in range(N):
        DP[i] = 1
        for j in range(i+1):
            if arr[j]<arr[i]:
                DP[i]=max(DP[j]+1,DP[i])
    print(max(DP))
#LIS 알고리즘 암기할것 !