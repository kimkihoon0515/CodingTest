n = int(input()) # n개의 숫자를 입력받는다.

x = list(map(int,input().split())) # 공백을 기준으로 x라는 list에 넣는다.
 
x2 = list(sorted(set(x))) # 새로운 list를 만들고 기존 list에서 중복된 것을 제거하고 순서대로 나열한다.

dic = {x2[i]:i for i in range(len(x2))} # 시간복잡도가 list형태는 O(N) 이고 index[i] 의 형태는 O(1) 이므로 dictionary indexing을 사용한다.

for i in x: 
    print(dic[i], end=" ")
