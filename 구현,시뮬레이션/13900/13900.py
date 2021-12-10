import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

answer = 0
sum = sum(li)
for i in li:
    sum -= i
    answer += sum*i
print(answer)