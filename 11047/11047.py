n,k = map(int,input().split())

a = []
for i in range(n):
    a.append(int(input()))
cnt = 0
while(k>0):
    cnt += k // a[n-1]
    k = k % a[n-1]
    n -= 1
print(cnt)