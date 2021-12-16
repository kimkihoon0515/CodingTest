import sys
from collections import deque

n,m,r = map(int,sys.stdin.readline().split())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def rotate(r):
    global n,m,li
    queue = deque()
    w,h = m,n
    time = min(w,h)//2
    nx,ny = 0,0
    
    while time >=1:
        for i in range(w-1):
            queue.append(li[ny][nx+i])
        for i in range(h-1):
            queue.append(li[ny+i][nx+w-1])
        for i in range(w-1):
            queue.append(li[ny+h-1][nx+w-1-i])
        for i in range(h-1):
            queue.append(li[ny+h-1-i][nx])
            
        queue.rotate(-r)
        
        for i in range(w-1):
            li[ny][nx+i] = queue.popleft()
        for i in range(h-1):
            li[ny+i][nx+w-1] = queue.popleft()
        for i in range(w-1):
            li[ny+h-1][nx+w-1-i] = queue.popleft()
        for i in range(h-1):
            li[ny+h-1-i][nx] = queue.popleft()
        
        w -= 2
        h -= 2
        nx +=1
        ny +=1
        time = min(w,h)//2

rotate(r)
for i in range(n):
    print(*li[i])