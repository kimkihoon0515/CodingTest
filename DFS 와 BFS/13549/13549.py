import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
maximum = 100001
visit = [-1 for i in range(maximum)] # -1 로 만드는 이유는 출발지점을 0으로 두고 -1 +1 *2 를 계산해서 갱신하기 위해서이다.
visit[n] = 0

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x = queue.popleft()
        if x == k:
            #print(visit)
            print(visit[x])
            break
        if 0 <= x-1 < maximum and visit[x-1] == -1: # 뒤로 가는것
            visit[x-1] = visit[x] + 1
            queue.append(x-1)

        if 0 <= 2*x < maximum and visit[2*x] == -1: # 순간이동 하는것, 순간이동 먼저 해서 이것이 정답이 되면 더 짧기 때문에 앞으로 한 칸 가는거보다 순간이동을 먼저 써줘야 한다.
            visit[2*x] = visit[x] # 순간이동을 먼저 넣어야하는 부분 때문에 자꾸 오류가 나서 많이 헤맸다.
            queue.appendleft(2*x)

        if 0 <= x+1 < maximum and visit[x+1] == -1: # 한 칸 앞으로 전진하는 것. 순간이동으로 도착하지 못했을 경우 차선책으로 사용
            visit[x+1] = visit[x] + 1
            queue.append(x+1)

bfs(n)