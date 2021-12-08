import sys

n = int(sys.stdin.readline())

cnt = 0

enter=dict()
out = []

for i in range(n):
    car = sys.stdin.readline().strip()
    enter[car] = i

for i in range(n):
    car = sys.stdin.readline().strip()
    out.append(car)

for i in range(n-1):
    for j in range(i+1,n):
        if enter[out[i]] > enter[out[j]]:
            cnt +=1
            break
print(cnt)