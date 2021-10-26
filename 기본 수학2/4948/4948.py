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
        break # 0을 입력받으면 break
    for i in prime_number: 
        if n < i <= 2 * n: # i가 n보다 크고 2n보다작을때까지 돌려서 배열에 있으면 cnt를 증가시킨다.
            cnt+=1
    print(cnt)
    cnt = 0 # 새로운n을 입력받기 전에 cnt를 0으로 초기화해준다.
    