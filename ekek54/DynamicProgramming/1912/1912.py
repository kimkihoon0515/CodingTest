import sys
import copy
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(' ')))
DP = copy.deepcopy(arr)
DP.insert(0,0)
for i in range(1,N+1):
    DP[i]=max(DP[i-1]+arr[i-1],arr[i-1])
print(max(DP[1:N+1]))