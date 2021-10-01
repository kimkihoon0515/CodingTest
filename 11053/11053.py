n = int(input()) # 수열의 숫자 수를 받는다.

li = list(map(int,input().split())) # 수열의 숫자들을 배열에 저장한다.

result = [1] * n # 1이 n개 있는 결과 배열을 만든다. 


for i in range(1,n): # 첫번째에는 1이 들어가고 그 다음부터는 규칙에 맞게 배열을 재정의한다.
    for j in range(i): # 이중배열을 선언해서 i번째까지 계속돌리는데
        if li[i]>li[j]: # 만약 i번쨰 li의 값이 최대라면 결과값을 i번째 결과값과 +1을 한 것중 최대값으로 잡는다.
            result[i] = max(result[i],result[j]+1)
print(max(result)) # 결과값들의 배열중 가장 큰 값을 출력한다.
