import sys

n,k = map(int,sys.stdin.readline().split())

ans = []
for i in range(1,n+1):
    if n%i == 0:
       ans.append(i) 
if len(ans) >= k:
    print(ans[k-1])
else:
    print(0)
    