n = int(input()) # 정수 n을 입력받는다.
i = 2
while n !=1:
    if n % i  == 0:
        n = n/i
        print(i)
    else : i += 1

