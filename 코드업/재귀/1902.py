import sys

def dfs(n):
    if n == 0:
        return
    print(n)
    dfs(n-1)
    
n = int(sys.stdin.readline())
dfs(n)