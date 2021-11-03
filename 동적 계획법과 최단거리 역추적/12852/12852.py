import sys

n = int(sys.stdin.readline())

result = [[0,[]] for _ in range(n+1)] # [최소값,경로 리스트]
result[1][0] = 0 # n이 1일때의 최소값
result[1][1] = [1] # n이 1일 때의 최소 경로 리스트


for i in range(2,n+1): # n이 2 이상일때
    result[i][0] = result[i-1][0] + 1 # -1을 할 경우
    result[i][1] = result[i-1][1] + [i] # -1을 할 경우의 최소 경로

    if i % 2 == 0 and result[i][0] > result[i//2][0] + 1: # 2로 나눌 경우
        result[i][0] = result[i//2][0] + 1
        result[i][1] = result[i//2][1] +[i] 

    if i % 3 == 0 and result[i][0] > result[i//3][0] + 1: # 3으로 나눌 경우
        result[i][0] = result[i//3][0] + 1
        result[i][1] = result[i//3][1] + [i]

print(result[n][0]) # 최소값 출력
result[n][1].reverse() # 최단 경로 출력
for i in result[n][1]:
    print(i,end=' ')
