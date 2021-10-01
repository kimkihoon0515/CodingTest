import sys
N= int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split(' '))) for i in range(N)]
# 최대 스케줄링은 먼저 끝나는것 우선으로 설정
#시작과 동시에 끝난느 경우 때문에 끝시간으로 정렬 후 시작시간에 대한 정렬도 필요함
arr.sort(key= lambda x:(x[1],x[0]))
sum=1
tmp = arr[0]
for i in range(1,len(arr)):
    if tmp[1]<=arr[i][0]:
        tmp=arr[i]
        sum+=1
print(sum)