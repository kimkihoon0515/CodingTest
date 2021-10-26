n = int(input()) # n개의 테스트 케이스를 입력받는다.
 
li = [1,1,1,2,2] # 규칙을 저장할 배열을 생성한다.

for i in range(6,100+1): # 규칙에 따라서 삼각형의 변의 길이를 추가한다.
    li.append(li[i-2]+li[i-6])


for _ in range(n): # 조건에 맞게 출력한다.
    a = int(input())
    print(li[a-1])
