import sys

n = int(sys.stdin.readline())

a,b,c,d=[],[],[],[]

for _ in range(n):
    A,B,C,D = map(int,sys.stdin.readline().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)

dic = {}

for i in a:
    for j in b:
        summary = i+j
        if summary in dic:
            dic[summary]+=1
        else:
            dic[summary] = 1

cnt = 0

for i in c:
    for j in d:
        summary = -1*(i+j)
        if summary in dic:
            cnt += dic[summary]

print(cnt)     
    