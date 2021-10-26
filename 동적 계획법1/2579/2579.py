n = int(input())

li = [0] * 301 # 계단을 입력받을 배열
result = [0] * 301 # 계단의 합의 최대값을 구할 배열
 
for i in range(n):
    li[i]=int(input())

result[0] = li[0]  # 첫 번째 계단은 항상 최대값
result[1] = li[0] + li [1] # 두 번쨰 계단도 항상 첫번째와 두번째 계단을 더한 값이 최대값
result[2] = max(li[1]+li[2], li[0]+li[2]) # 3번째 계단은 두번째계단 + 세 번째 계단 또는 첫번째 계단 + 세번째 계단

for i in range(3,n): # 4번째부터는 조건에 맞게 배열에 저장한다.
    result[i] = max(result[i-3]+li[i-1]+li[i],result[i-2] + li[i]) 
print(result[n-1])