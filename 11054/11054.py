n = int(input()) # 숫자 n개를 입력받는다.

li= list(map(int,input().split())) # 입력받은 숫자들을 배열에 저장한다.

increase = [1] * n # 증가하는 배열을 만든다.
decrease = [1] * n # 감소하는 배열을 만든다.
result = [] # 증가수열의 최대값을 저장하는 배열

for i in range(n): # 증가하는 수열(왼쪽 수열)
    for j in range(i):
        if li[i] > li[j] and increase[i] <increase[j]+1:
            increase[i] = increase[i] +1

for i in range(n-1,-1,-1): # 감소하는 수열(오른쪽 수열)
    for j in range(n-1,i,-1):
        if li[i] > li[j] and decrease[i] < decrease[j] +1:
            decrease[i] = decrease[j] + 1
    result.append(decrease[i]+increase[i]-1) # 겹치는 것 한개가 있으므로 빼준다.
print(max(result))
        


