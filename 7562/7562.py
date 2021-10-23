from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    queue = deque()
    queue.append([sx, sy])
    li[sx][sy] = 1
    while queue:
        a, b = queue.popleft()
        if a == ax and b == ay:
            print(li[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < l and 0 <= y < l and li[x][y] == 0:
                queue.append([x, y])
                li[x][y] = li[a][b] + 1
t = int(input())
for i in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    li = [[0] * l for i in range(l)]
    bfs(sx, sy, ax, ay)