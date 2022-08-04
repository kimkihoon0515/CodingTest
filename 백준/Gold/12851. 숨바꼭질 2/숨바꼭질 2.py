import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
# -1,+1,*2 중 하나

visit = [-1 for _ in range(100001)]

cnt = 0

def bfs(n):
    global cnt
    queue = deque()
    queue.append(n)
    visit[n] = 0

    while queue:
        x = queue.popleft()
        if x == k:
            cnt+=1
        op = [x-1,x+1,x*2]
        for i in op:
            if 0<=i<100001:
                if visit[i] == -1 or visit[i] == visit[x]+1:
                    queue.append(i)
                    visit[i] = visit[x] + 1
    
bfs(n)
print(visit[k])
print(cnt)