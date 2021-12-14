import sys

x,y = map(int,sys.stdin.readline().split())
answer = 0
if y*100//x >= 99: # 바꿀 때 int말고 분모에 100 곱해서 x로 나누는 방법으로 해야함
    answer = -1
else:
    left = 1
    right = x
    while left<=right:
        mid = (left+right)//2
        new_x = mid + x 
        new_y = mid + y
        if new_y*100//new_x > y*100//x:
            answer = mid
            right = mid -1
        else:
            left = mid +1
print(answer)