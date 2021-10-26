import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
result = [0]

for i in range(n):
    start = 0 # 시작점은 0
    end = len(result) -1 # 끝점은 결과 배열의 길이 -1
    while start <= end:
        #print('start = ',start)
        #print('end = ',end)
        #print('result = ',result )
        mid = (start+end) //2 # 중앙값을 정한다.
        if result[mid]< li[i]: # 결과배열의 가장 큰 값보다 i번째 입력값 배열이 크면 
            start = mid+1 # 시작점을 옮긴다.
        else: # 그렇지않으면 끝점을 줄인다.
            end = mid-1
    if start >= len(result): # 만약 li[i]번째 배열이 결과배열의 마지막 값보다 크면 그 값을 넣는다.
        result.append(li[i])
    else: 
        result[start] = li[i]
print(len(result)-1)
