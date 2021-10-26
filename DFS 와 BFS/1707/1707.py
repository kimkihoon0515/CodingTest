# 너무 어려워서 그냥 참고함.
import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(v):
    queue = deque([v])
    visit[v] = 1
    while queue:
        x = queue.popleft()
        for i in li[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                queue.append(i)
            if visit[i] == visit[x]:
                return False
    return True

for _ in range(k):
    v,e = map(int,sys.stdin.readline().split())
    li = [[]for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    isTrue = True

    for _ in range(e):
        a,b = map(int,sys.stdin.readline().split())
        li[a].append(b)
        li[b].append(a)

    for i in range(1,v+1):
        if visit[i] == 0:
            if not bfs(i):
                isTrue = False
                break
    print('YES' if isTrue else 'NO')