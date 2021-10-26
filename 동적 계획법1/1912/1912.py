n = int(input()) # 숫자의 개수를 입력받는다.

li = list(map(int,input().split())) # 숫자들을 배열에 넣어 저장한다.
result=[] # 합의 최대값들을 넣을 배열
result.append(li[0]) # 첫 번째는 그냥 넣어준다. 
for i in range(n-1): # 2번째부터는 새로 들어온 숫자와 그 이전까지의 배열합의 최대값을 비교하여 더 큰쪽을 남겨둔다.
    result.append(max(result[i]+li[i+1],li[i+1])) 

print(max(result)) # 최대값을 출력한다.
