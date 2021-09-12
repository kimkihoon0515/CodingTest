import sys
N = int(sys.stdin.readline())
DP=[0,1,1]
if N < 4:
    print(DP[N-1])
else:
    for i in range(4,N+1):
        if i % 6 ==0:
            DP.append(min(DP[i//3-1],DP[i-2],DP[i//2-1])+1)
        elif i % 3 ==0:
            DP.append(min(DP[i//3-1],DP[i-2])+1)
        elif i % 2 ==0:
            DP.append(min(DP[i-2],DP[i//2-1])+1)
        else:
            DP.append(DP[i - 2] + 1)
    print(DP[N-1])