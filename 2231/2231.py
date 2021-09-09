n = int(input()) # 자연수 n을 입력받는다.
result = 0

for i in range(1,n+1): 
    a = list(map(int,str(i))) # i의 자리수의 배열을 만든다.
    s = i + sum(a) # 자리수 + 실제값
    if(s == n ): # 같으면 result를 출력한다.
        result = i
        break
print(result)