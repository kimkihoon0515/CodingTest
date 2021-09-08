import math
t = int(input()) # 테스트 케이스 T를 입력받는다.

for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split()) 
    distance = math.sqrt(abs(x2-x1)**2 + abs(y2-y1) **2)
    add = r1 + r2
    sub = abs(r1-r2)
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance == add or distance == sub:
            print(1)
        elif sub<distance<add :
            print(2)
        else:
            print(0)
