import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

a = deque(list(map(int,sys.stdin.readline().split()))) # 컨베이어 벨트의 내구도
robot = deque([0 for i in range(2*n)]) # 각 칸마다 존재하는 로봇의 수
ans = 1 # 결과값

def rotate(): 
    robot.rotate(1) # 로봇을 1만큼 회전시킨다.
    a.rotate(1) # 컨테이너를 1만큼 회전시킨다.

cnt = 0 # 내구성이 0이 된 개수

def move():
    global cnt
    for i in range(n-2,-1,-1): # 가장 먼저 벨트에 올라간 로봇 순서부터 -1 씩 해준다.
        if robot[i]>0 : # 로봇이 있다면
            move = i+1 # 바로 다음 칸
            if a[move] >0 and robot[move] == 0: # 한칸 앞의 내구도가 남아 있고 그 칸에 로봇이 없으면
                a[move] -= 1 # 내구도를 1 감소시키고
                robot[move] = 1 # 로봇을 한 칸 앞으로 옮긴다.
                robot[i] = 0 # 그 전칸의 로봇은 없애준다.
                if a[move] == 0: # 내구도가 없다면
                    cnt += 1 # 내구도 없는 개수를 1 증가

while True:
    rotate() # 한번 회전한다.
    robot[n-1] = 0 # 로봇을 내린다.
    move() # 하나씩 옮긴다.
    robot[n-1] = 0 # 로봇을 내린다.
    
    if a[0] > 0 and robot[0] == 0: # 만약 벨트의 시작지점에 내구도가 남아 있고 로봇이 없다면
        robot[0] = 1 # 로봇을 올리고 
        a[0] -= 1 # 내구도를 하나 감소시킨다.
        if a[0] == 0: # 만약 내구도가 없다면
            cnt += 1 # 내구도가 없는 개수를 하나 증가시킨다.
    if cnt >= k: # 결과값 출력
        print(ans)
        break
    ans += 1 # 결과값의 조건이 맞을 때까지 하나씩 올린다.