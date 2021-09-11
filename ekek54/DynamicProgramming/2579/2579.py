import sys
N = int(sys.stdin.readline())
if N ==1: #계단 한칸인 경우 예외처리
    print(int(sys.stdin.readline()))
else:
    arr = [int(sys.stdin.readline()) for i in range(N)]
    arr.insert(0,0)
    DP = [0 for i in range(N+1)]
    DP[1] = arr[1]
    DP[2] = arr[1]+arr[2]
    if N>3:
        for i in range(3,N+1):
            DP[i] = max(arr[i-1]+DP[i-3],DP[i-2])+arr[i]
    print(DP[N])