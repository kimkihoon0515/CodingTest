import sys
N = int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for i in range(N)]
arr.insert(0,0)
if N < 2:
    print(arr[N])
else:
    DP=[0,arr[1],arr[1]+arr[2]]
    if N>2:
        for i in range(3,N+1):
            DP.append(max(DP[i-1],DP[i-2]+arr[i],DP[i-3]+arr[i-1]+arr[i]))

    print(DP[N])