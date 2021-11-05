from collections import deque
import sys

t = int(sys.stdin.readline())

def bfs():
    queue = deque()
    queue.append([a,""])
    visited[a] = 1
    while queue:
        x,y = queue.popleft()
        if x == b:
            print(y)
        d = (x*2) % 10000 # d는 (n * 2) % 10000 한 값을 저장한다. 
        if not visited[d]:
            visited[d] = 1 # d는 탐색했으므로 
            queue.append([d,y+'D']) # queue에 시작값과 계산식을 넣는다.
        if x !=0: # queue 의 시작값이 0이아니면 1을 빼고 0이면 9999를 넣는다.
            s = x - 1
        else:
            s = 9999
        if not visited[s]:
            visited[s] = 1 # s를 탐색했으므로 1로 바꿔준다.
            queue.append([s,y+'S']) # queue 에 시작값과 계산식을 넣는다.
        l = x % 1000 * 10 + x // 1000 # 각 자리를 왼편으로 회전시킨다.
        if not visited[l]: 
            visited[l] = 1 # l을 탐색했으므로 1로 바꿔준다.
            queue.append([l,y+'L']) # queue에 시작값과 계산식을 넣는다.
        r = x % 10 * 1000 + x // 10 # 각 자리를 오른쪽으로 회전시킨다.
        if not visited[r]:
            visited[r] = 1 # r을 탐색했으므로 1로 바꿔준다.
            queue.append([r,y+'R']) # queue에 시작값과 계산식을 넣는다.

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    visited = [0 for _ in range(10000)] 
    bfs()