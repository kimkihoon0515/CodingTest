import sys

n = int(sys.stdin.readline().strip())

a = list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    a[i] +=a[i-1]

m = int(sys.stdin.readline())

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    i = i-1
    if i == 0:
        print(a[j-1])
    else:
        print(a[j-1]-a[i-1])
    