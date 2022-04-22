import sys
from collections import deque

def check():
    visited = [[False for _ in range(5)] for _ in range(5)]
    for index in arr:
        visited[index // 5][index % 5] = True

    que = deque([arr[0]])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    depth = 0
    visited[arr[0] // 5][arr[0] % 5] = False

    while que :
        index = que.popleft()
        depth += 1
        y = index // 5
        x = index % 5

        for dy, dx in dir :
            yy, xx = dy + y, dx + x
            if 0 <= yy < 5 and 0 <= xx < 5 and visited[yy][xx]:
                visited[yy][xx] = False
                que.append((5 * yy) + xx)

    if depth == 7:
        return True
    else :
        return False

def DFS(depth,index,s_cnt, y_cnt):
    global cnt

    if depth == 7 and s_cnt >= 4:
        if check():
            cnt += 1
        return

    if y_cnt >= 4 or index >= 25 or depth > 7:
        return

    y = index // 5
    x = index % 5

    arr.append(index)
    if table[y][x] == 'Y':
        DFS(depth + 1, index + 1, s_cnt, y_cnt + 1)
    elif table[y][x] == 'S':
        DFS(depth + 1, index + 1, s_cnt + 1, y_cnt)
    arr.pop()
    DFS(depth, index+1, s_cnt, y_cnt)

table = [list(map(str, sys.stdin.readline().rstrip("\n"))) for _ in range(5)]

cnt,arr = 0,[]
DFS(0,0,0,0)
print(cnt)