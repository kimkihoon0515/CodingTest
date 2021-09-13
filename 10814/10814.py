n = int(input())

person = []
for i in range(n):
    age,name = map(str,input().split())
    age = int(age)
    person.append([age,name])
person.sort(key=lambda x:x[0])

for i in range(len(person)):
    print(person[i][0],person[i][1])