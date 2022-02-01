import sys

m,n = map(int,sys.stdin.readline().split())
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
dic = dict()
for i in range(10):
    dic[str(i)] = numbers[i]
print(dic)

li = []
for i in range(m,n+1):
    s = ''.join([dic[j] for j in str(i)])
    li.append([i,s])
li.sort(key=lambda x:x[1])

for i in range(len(li)):
    if i%10 == 0 and i != 0:
        print()
    print(li[i][0],end = ' ')
        