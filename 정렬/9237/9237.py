import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

li.sort(reverse=True)

for i in range(len(li)):
    li[i] = li[i]+(i+1)

print(max(li)+1)