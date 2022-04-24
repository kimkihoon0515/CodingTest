import sys

n,m = map(int,sys.stdin.readline().split())

li = sorted(list(map(int,sys.stdin.readline().split())))

ans = []

def dfs(index):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(index,n):
        if li[i] not in ans:
            ans.append(li[i])
            dfs(i+1)
            ans.pop()
dfs(0)