import sys
arr = list(sys.stdin.readline().rstrip('\n').split('-'))
res=[]
for i in arr:
    if '+' in i:
        tmp = i.split('+')
        sum=0
        for j in tmp:
            sum += int(j)
        i = sum
        res.append(i)
    else:
        i = int(i)
        res.append(i)
for i in res[1:]:
    res[0]-=i
print(res[0])

