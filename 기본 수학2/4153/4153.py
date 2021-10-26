max = 0 # a,b,c중 최대 값을 받을 변수
while True: 
    a,b,c = map(int,input().split()) # a,b,c를 입력받는다.
    if a == 0 and b == 0 and c == 0: # 셋 다 0을 입력받으면 멈추고
        break
    else:
        if a < b:
            max = b
            if max < c:
                max = c
        else:
            max = a
            if max < c:
                max = c # 최대값을 구해준다.
    if a**2 + b ** 2 + c **2 == 2 * max ** 2: # 피타고라스의 정리를 사용해서 만약 0 이면 right를 아니면 wrong을 출력한다.
        print("right")
    else:
        print("wrong")
