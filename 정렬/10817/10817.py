import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

li = sorted(li)

answer = []

for i in li:
    if i not in answer:
        answer.append(i)

print(*answer)