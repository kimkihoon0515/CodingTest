import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

a = sorted(li)

ans = []

for i in range(n):
    ans.append(a.index(li[i]))
    a[a.index(li[i])] = -1

print(*ans)