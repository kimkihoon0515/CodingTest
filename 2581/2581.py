m = int(input()) # 자연수 M 을 입력받는다.
n = int(input()) # 자연수 N 을 입력받는다.

def is_prime_number(x): # 소수를 판별하는 알고리즘
    if x == 1: 
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

first_number=0 # 범위 내에 가장 첫 번째 소수를 저장하는 변수
sum = 0 # 범위 내 소수들의 합
cnt = 0 # 가장 첫 번째 소수를 계산하기 위해서 필요한 변수
for i in range(m,n+1): # 입력값들의 범위만큼 반복문을 돌린다.
    if is_prime_number(i) == True: # 소수인지 판별하고 가장 첫 번째 소수를 first_number에 저장한다.
        cnt+=1
        if cnt == 1:
            first_number = i
        sum+=i # 소수들의 합을 구한다.
    else:
        cnt+=0
if cnt==0: # 범위 내 소수가 없으면 -1을 출력
    print(-1)
else: 
    print(sum)
    print(first_number)

        