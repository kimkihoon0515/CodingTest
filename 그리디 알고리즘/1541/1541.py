s = input().split('-') # 입력값을 - 가 있는 부분과 없는 부분으로 나눈다.
result = 0 # 결과값을 저장하는 변수
for i in s[0].split('+'): # -가 나오기 전까지는 전부 더한다.
    result +=int(i)
for i in s[1:]: # 그리고 그 다음부터는 -가 나오므로 모든 숫자를 빼주면 된다.
    for j in i.split('+'):
        result -=int(j)
print(result)