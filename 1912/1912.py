n = int(input())

li = list(map(int,input().split()))
result=[]
result.append(li[0])
for i in range(n-1):
    result.append(max(result[i]+li[i+1],li[i+1]))

print(max(result))
