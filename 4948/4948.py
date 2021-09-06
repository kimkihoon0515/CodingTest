def is_prime_number(x): # 소수를 판별하는 알고리즘
    if x == 1: 
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

prime_number=[] # 소수인 배열을 저장하기 위해서 선언
for i in range(2,246912): # 범위를 1 ~ 123456까지 한정해놓고 소수들만 집어넣는다.
    if is_prime_number(i)==True:
        prime_number.append(i)

cnt = 0 # 소수의 개수를 판별하기위한 변수



while True:
    n = int(input()) # 입력을 받는다.
    if n == 0:
        break
    for i in prime_number:
        if n < i <= 2 * n:
            cnt+=1
    print(cnt)
    cnt = 0
    