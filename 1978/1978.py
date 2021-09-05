n = int(input()) # 수의 개수 n을 입력받는다.
cnt = 0
a = list(map(int,input().split()))

for i in a:
    if i !=1:
        for j in range(2,i):
            if i % j == 0 :
                break
        else:
            cnt+=1
print(cnt)