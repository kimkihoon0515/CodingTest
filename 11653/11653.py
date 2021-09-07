n = int(input()) # 정수 n을 입력받는다.

i = 2 # 소수인 2부터 시작

while n !=1 :
    if n % i  == 0: # n을 i로 계속 나누는데 나머지가 0이 아닐때까지 나눈다.
        n = n/i
        print(i)
    else : i += 1

