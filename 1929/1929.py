m, n = map(int,input().split())

def is_prime_number(x): # 소수를 판별하는 알고리즘
    if x == 1: 
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(m,n+1):
    if is_prime_number(i) == True:
        print(i)
