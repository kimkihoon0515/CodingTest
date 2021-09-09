n = int(input()) # 자연수 n을 입력받는다.
result = 0

for i in range(1,n+1):
    a = list(map(int,str(i)))
    s = i + sum(a)
    if(s == n ):
        result = i
        break
print(result)