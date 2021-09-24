import sys
arr_1 = list(sys.stdin.readline().rstrip('\n'))
arr_2 = list(sys.stdin.readline().rstrip('\n'))
arr_1.insert(0,0)
arr_2.insert(0,0)
DP=[[0 for i in range(len(arr_1))] for _ in range(len(arr_2))]
for i in range(1,len(arr_2)):
    for j in range(1,len(arr_1)):
        if arr_1[j] == arr_2[i]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])
print(max(map(max,DP)))