n = int(input()) # 테스트 케이스의 개수를 입력받는다.
cnt = 1

for i in range(n): 
    x,y = map(int,input().split()) # x,y를 입력받고 그 거리를 계산한다.
    distance = y - x

    while True:
       if cnt**2 <=distance<(cnt+1)**2: 
           break
       cnt +=1 # 계속해서 한번 이동하는 거리를 증가시킨다.
    if distance == cnt**2: # 총 이동거리가 cnt의 제곱과 같을 때 
        print(cnt*2-1)
    elif cnt ** 2 < distance <= cnt**2 + cnt: # 총 이동거리가 cnt의 제곱보다 크고 cnt제곱 +cnt 보다 작거나 같을 때
        print(cnt*2)
    else: 
        print(cnt*2+1)
        
