import sys

n = int(sys.stdin.readline().strip())

li = list(map(int,sys.stdin.readline().split()))

answer = [0 for i in range(n)]

for i in range(1,n+1):
    height = li[i-1]
    cnt = 0
    for j  in range(n):
        if cnt == height and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            cnt +=1
print(*answer)