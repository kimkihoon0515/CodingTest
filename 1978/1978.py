n = int(input()) # 수의 개수 n을 입력받는다.
cnt = 0 # 소수의 개수를 저장하기 위한 변수
a = list(map(int,input().split())) # 공백으로 구분지어서 숫자를 입력받는다/

for i in a:
    if i !=1: # i가 1이 아닐경우에는
        for j in range(2,i): # 2 부터 i 까지 반복문을 돌려서
            if i % j == 0 : # 1과 자기자신을 제외한 수로 나누어지면 안세고
                break
        else:
            cnt+=1 # 나누어지지않으면 개수를 하나 늘린다.
print(cnt)