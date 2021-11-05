import sys

n,k = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a.sort()
b.sort()
b.reverse()
tmp = 0
for i in range(k):
    if a[i] < b[i]:
        tmp = a[i]
        a[i] = b[i]
        b[i] = tmp
    else:
        break

print(sum(a))
