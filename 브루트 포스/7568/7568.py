n = int(input()) # 몇 개를 입력받을 것인지 정하는 변수
student=[] # 학생들의 몸무게와 키를 저장할 배열
ans = [] # 등수를 저장할 배열
for i in range(n): # 학생들의 키와 몸무게를 배열에 저장한다.
    x,y = map(int,input().split())
    student.append((x,y))

for i in range(n): # 등수를 계산하는 알고리즘
    cnt = 0 
    for j in range(n):
        if student[i][0] < student[j][0] and student[i][1] < student[j][1]: # 몸무게와 키가 더 많으면
            cnt+=1 # cnt를 하나씩 늘린다.
    ans.append(cnt+1) 

for i in ans:
    print(i,end=" ")