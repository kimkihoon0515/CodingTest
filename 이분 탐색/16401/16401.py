import sys

m,n = map(int,sys.stdin.readline().split())

l = list(map(int,sys.stdin.readline().split()))

left = 1
right = max(l)

ans = 0
while left <= right:
    mid = (left+right) // 2
    cnt = 0 # 막대 과자의 개수
    
    if mid == 0: # mid가 0이 될 때까지 막대과자를 못 나눠주는 경우
        ans = 0 # 0을 대입한다.
        break
    
    for i in l: # 막대과자의 개수를 구하는 반복문
        if i >= mid:
           cnt += i//mid
           
    if cnt >= m: # m개 보다 많아지면
        left = mid + 1 # 왼쪽에서 조정
        ans = mid 
        
    else: # m개보다 적으면 
        right = mid - 1 # 오른쪽에서 조정
        
print(ans) 