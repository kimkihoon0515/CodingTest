import sys

a,b = map(int,sys.stdin.readline().split())
ans = []
def dfs(idx,n):
    if idx > n:
        return
    if idx%2!=0:
        ans.append(idx)
    dfs(idx+1,n)
    
dfs(a,b)
print(*ans)