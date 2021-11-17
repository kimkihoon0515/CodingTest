import sys
from collections import deque

a,b,c = map(int,sys.stdin.readline().split())

visit = [[0 for i in range(201)] for _ in range(201)]

result = []

def bfs():
    queue = deque()
    queue.append([0,0,c])

    while queue:
        x,y,z = queue.popleft()
        if visit[x][z] == 1: # 탐색안한곳만 탐색해야하므로 없으면 메모리 초과남
            continue
        else:
            visit[x][z] = 1
        if x == 0: # 결과값에 넣는다.
            result.append(z)
        if x + y > b: # a -> b
            queue.append([x + y - b, b, z])
        else: 
            queue.append([0, x + y, z])
        if x + z > c: # a -> c
            queue.append([x + z - c, y, c])
        else: 
            queue.append([0, y, x + z])
        if y + x > a: # b -> a
            queue.append([a, y + x - a, z])
        else: 
            queue.append([y + x, 0, z])
        if y + z > c: # b -> c
            queue.append([x, y + z - c, c])
        else: 
            queue.append([x, 0, y + z])
        if z + x > a: # c -> a
            queue.append([a, y, z + x - a])
        else: 
            queue.append([z + x, y, 0])
        if z + y > b: # c -> b
            queue.append([x, b, z + y - b])
        else: 
            queue.append([x, z + y, 0])

bfs()
result.sort()
print(*result)