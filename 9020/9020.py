t = int(input()) # 테스트 케이스 T를 입력받는다.

def is_prime_number(x): # 소수를 판별하는 알고리즘
    if x == 1: 
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

prime_number=[]
for i in range(2,10000):
    if is_prime_number(i) == True:
        prime_number.append(i)

sub = 0

for i in range(t):
    n = int(input())
    sub = n // 2
   
    if is_prime_number(sub) == False:
        for j in range(1,sub):
            a = sub - j
            b = sub + j
            if is_prime_number(a) == True and is_prime_number(b) == True:
                print(a,b)
                break
    else:
        print(sub,sub)
        
