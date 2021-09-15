import sys
N = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split(' ')))
arr_rev=list(reversed(arr))
LIS= [0 for i in range(N)]
LDS= [0 for i in range(N)]
if N ==1:
    print(1)
else:
    for i in range(N):
        LIS[i] = 1
        LDS[i] = 1
        for j in range(i+1):
            if arr[j]<arr[i]:
                LIS[i]=max(LIS[j]+1,LIS[i])
            if arr_rev[j]<arr_rev[i]:
                LDS[i]=max(LDS[j]+1,LDS[i])
    LDS.reverse()
    for i in range(N):
        LIS[i]+=LDS[i] - 1
    print(max(LIS))
#LIS 알고리즘 암기할것 !
#입력 리스트를 역순으로 LIS 알고리즘을 돌리면 가장 긴 감소하는 부분 수열을 구할 수 있음
#DP 리스트를 N번 쩨 값이 중간 값인 가장긴 바이토닉 수열의 길이라고 생각하면 DP[N] 값은 LIS[N]+LDS[N] - 1 로 구할 수 있다.
