import sys

n,m = map(int,sys.stdin.readline().split())

li = sorted(list(map(int,sys.stdin.readline().split())))

answer = []

def dfs(index,n,m):
    if index == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(n):
        answer.append(li[i])
        dfs(index+1,n,m)
        answer.pop()
dfs(0,n,m)
