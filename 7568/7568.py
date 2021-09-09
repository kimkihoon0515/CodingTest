n = int(input())
student=[]
ans = []
for i in range(n):
    x,y = map(int,input().split())
    student.append((x,y))
print(student)
for i in range(n):
    cnt = 0
    for j in range(n):
        if student[i][0] < student[j][0] and student[i][1] < student[j][1]:
            cnt+=1
    ans.append(cnt+1)

for i in ans:
    print(i,end=" ")