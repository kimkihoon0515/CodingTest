import sys

x,y = map(int,sys.stdin.readline().split())
answer = 0
if y*100//x >= 99:
    answer = -1
else:
    left = 1
    right = x
    while left<=right:
        mid = (left+right)//2
        new_x = mid + x 
        new_y = mid + y
        if new_y*100//new_x == y*100//x:
            left = mid +1
        else:
            answer = mid
            right = mid -1
print(answer)