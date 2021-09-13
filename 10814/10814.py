n = int(input()) # n개의 입력값을 입력받는다.

person = []
for i in range(n): 
    age,name = map(str,input().split()) # 나이와 이름을 입력받는다 
    age = int(age) # 나이는 int 형식으로 변환하고 배열에 넣는다.
    person.append([age,name]) 
person.sort(key=lambda x:x[0]) # 나이 순으로 정렬한다.

for i in range(len(person)):
    print(person[i][0],person[i][1])