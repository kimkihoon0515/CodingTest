import sys

def dfs(idx,n):
    if idx == n:
        return
    print(idx+1)
    dfs(idx+1,n)

n = int(sys.stdin.readline())
dfs(0,n)