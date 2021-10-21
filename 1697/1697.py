import sys
from collections import deque

maximum = 100000              
li = [0 for i in range(maximum+1)] # 이동거리를 저장하기 위한 배열
n, k = map(int,sys.stdin.readline().split())
queue = deque()
def bfs():
    queue.append(n) # 시작점을 queue 에 저장한다.             
    while  queue:
        x = queue.popleft() # 이동거리를 x로 두고
        if x == k: # x가 도착점이랑 같아지면 출력
            print(li[x])
            break
        for i in (x - 1, x + 1, x * 2): # -1,+1,x2 하나씩 돌려보면서 queue에 넣는다.
            if 0 <= i <= maximum and not li[i]:
                li[i] = li[x] + 1 # 이동 거리를 하나씩 늘려서 저장한다.
                queue.append(i) # queue에 얼마나 이동했는지 그 거리를 저장한다.

bfs()
