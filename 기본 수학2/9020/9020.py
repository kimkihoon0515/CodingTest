t = int(input()) # 테스트 케이스 T를 입력받는다.

def is_prime_number(x): # 소수를 판별하는 알고리즘
    if x == 1: 
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

prime_number=[] # 소수를 넣기 위한 배열을 선언해준다. 

for i in range(2,10000): # 에라토스테네스의 체를 이용한다.
    if is_prime_number(i) == True:
        prime_number.append(i)

sub = 0

for i in range(t):
    n = int(input())
    sub = n // 2 # 반으로 나눈 값에서 시작한다.
   
    if is_prime_number(sub) == False: # 만약 소수가아니면 
        for j in range(1,sub): # a는 1씩 빼고 b는 1씩 증가시킨다.
            a = sub - j
            b = sub + j
            if is_prime_number(a) == True and is_prime_number(b) == True: # 만약 소수인데 합이 n인 경우를 반견하면 출력하고 반복문을 멈춘다.
                print(a,b) # 중앙에서 1씩 빼기때문에 가장 처음값이 가장 최소 값이다.
                break
    else:
        print(sub,sub) # 만약 소수가아니면 그냥 2로 나눈 값을 출력한다.
        
