import sys
N = int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split(' '))) for i in range(N)]
arr.sort()
LIS= [0 for i in range(N)]
if N ==1:
    print(1)
else:
    for i in range(N):
        LIS[i] = 1
        for j in range(i+1):
            if arr[j][1]<arr[i][1]:
                LIS[i]=max(LIS[j]+1,LIS[i])
    print(N-max(LIS))
#왼쪽 전봇대를 기준으로 증가하는 순서로 탐색하는 겅우 오른쪽 전봇대의 가장 긴 증가 부분수열이 가장 많은 전깃줄 개수가 된다.
# 가장 많은 전깃 줄 개수는 없애야 하는 전깃줄의  개수가 최소임을 의미