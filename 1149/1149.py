n = int(input())

li = []

for i in range(n):
    li.append(list(map(int,input().split())))


for i in range(1,len(li)):
    li[i][0] = min(li[i-1][1],li[i-1][2])+li[i][0]
    li[i][1] = min(li[i-1][0],li[i-1][2])+li[i][1]
    li[i][2] = min(li[i-1][0],li[i-1][1])+li[i][2]
print(min(li[n-1][0],li[n-1][1],li[n-1][2]))