import sys

n,m = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))
li = sorted(li)

visit = [False for _ in range(n)]

def dfs(index):
    if index == m:
        print(' '.join(list(map(str,index))))
        return
    