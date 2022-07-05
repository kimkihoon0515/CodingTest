import sys

n,s = map(int,sys.stdin.readline().split())

cos = [int(sys.stdin.readline().strip()) for _ in range(n)]
cos.sort()

left = 0
right = 1
cnt = 0

for start in range(n):
    right = start+1
    while right < n:
        if cos[start]+cos[right]>s:
            break
        else:
            cnt +=1
            right +=1
print(cnt)