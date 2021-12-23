import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

answer = 0
for i in range(1,m):
    answer = max(answer,li[i]-li[i-1])
    
print(max((answer+1)//2,li[0]-0,n-li[-1])) # 중앙값과 양끝까지의 값 중 가장 큰 값을 출력해야함.
