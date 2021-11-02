"""
에라토스테네스의 체로 소수를 먼저 구하고 투 포인터 알고리즘을 사용해야함. 
"""
import sys

n = int(sys.stdin.readline())

arry = [False,False] + [True] * (n-1) # 에라토스테네스의 체로 소수를 구하는 알고리즘
prime_num = []

for i in range(2,n+1):
    if arry[i]:
        prime_num.append(i)
    for j in range(i*i,n+1,i):
        arry[j] = False

sum = 0
right = 0
left = 0
cnt = 0

while True: 
    if sum >= n: # 합이 n이상일때
        if sum == n: # n과 같다면
            cnt +=1 # cnt를 하나 증가시킴
        sum -=prime_num[left] # 가장 왼쪽의 소수를 합에서 빼주고 left를 하나 증가시킴
        left +=1
    elif right == len(prime_num): # 만약 오른쪽과 소수의 개수가 같아지면 멈춘다.
        break
    else:
        sum +=prime_num[right] # 합이 작고 아직 끝에 도달하지 못했다면 합을 늘려주고 오른쪽도 하나씩 증가시킨다.
        right +=1
print(cnt)