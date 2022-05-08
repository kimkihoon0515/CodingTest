import sys

n = int(sys.stdin.readline().strip())

li = sorted(list(map(int,sys.stdin.readline().split())))

answer = 0

for i in li:
    if answer+1 >= i:
        answer += i
    else:
        break
print(answer+1)

