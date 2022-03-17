import sys

n = int(sys.stdin.readline())

result = 0
sum = 0
end = 1

for i in range(1,n+1): # 기존에 해왔던대로 list를 선언하면 메모리 오류 발생
    while sum < n and end < n: # 합이 n보다 작고 가장 큰 숫자도 n보다 작은 경우 반복문 돌림
        sum += end # 합계에 연속된 숫자를 더해준다
        end +=1 # 숫자를 하나씩 증가시킨다.
    if sum == n: # n과 같아지면
        result += 1 # 답을 1개 증가시킨다.
    sum -= i # 가장 작은 수를 합에서 빼준다.
print(result+1) # n 자체로 만족하는 경우 하나 더 추가