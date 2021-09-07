max = 0
while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a < b:
            max = b
            if max < c:
                max = c
        else:
            max = a
            if max < c:
                max = c
    if a**2 + b ** 2 + c **2 == 2 * max ** 2:
        print("right")
    else:
        print("wrong")
