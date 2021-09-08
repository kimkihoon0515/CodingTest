n = int(input()) # 입력값 n을 입력받는다.
factorial = 1
for i in range(1,n+1):
    factorial *=i
print(factorial)