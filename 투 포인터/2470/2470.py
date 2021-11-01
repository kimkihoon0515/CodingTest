import sys

n = int(sys.stdin.readline())

li = sorted(list(map(int,sys.stdin.readline().split())))

cnt = 0
left = 0
right = n-1
ans = sys.maxsize

result = []
while left < right:
    sum = li[left] + li[right]
    if abs(sum) < ans:
        ans = abs(sum)
        result=[li[left],li[right]]
    
    if sum < 0:
        left +=1
    else:
        right -=1
print(result[0],result[1])