import math
t = int(input()) # 테스트 케이스 T를 입력받는다.

for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split()) # 입력값을 입력받는다.
    distance = math.sqrt(abs(x2-x1)**2 + abs(y2-y1) **2) # 두 원점 사이의 거리를 구한다.
    add = r1 + r2 # 두 반지름의 합을 구한다.
    sub = abs(r1-r2) # 두 반지름의 차를 구한다.
    if distance == 0: # 두 원점 사이의 거리가 0일 때 
        if r1 == r2: # 반지름의 길이가 같으면 원이 같으므로 무한대로 만난다.
            print(-1) 
        else: # 반지름의 길이가 다르면 만나지 않는다.
            print(0)
    else: 
        if distance == add or distance == sub: # 두 원점 사이의 거리가 합이나 차와 같으면 한 점에서 만난다.
            print(1)
        elif sub<distance<add: #두 원점 사이의 거리가 두 반지름의 합과 차 사이값이면 두 점에서 만난다.
            print(2)
        else: # 아니면 만나지 않는다.
            print(0)
