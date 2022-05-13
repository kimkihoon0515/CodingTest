import sys

n = int(sys.stdin.readline())

people = []

for _ in range(n):
    name,day,month,year = map(str,sys.stdin.readline().split())
    people.append([str(name),int(day),int(month),int(year)])

people = sorted(people,key=lambda x: (x[3],x[2],x[1]))
print(people[-1][0],people[0][0])