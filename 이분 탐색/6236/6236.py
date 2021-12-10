import sys

n,m = map(int,sys.stdin.readline().split())

li = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = min(li)
right = sum(li)

while left <= right:
    mid = (left+right)//2
    a = mid
    cnt = 1
    for i in li:
        if mid < i:
            mid = a
            cnt +=1
        mid -= i
    
    if cnt > m or a < max(li):
        left = a+1
    else:
        right = a -1
        k = a    
print(k)