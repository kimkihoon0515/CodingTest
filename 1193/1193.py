x = int(input())

cnt = 1

while x >cnt:
    x-=cnt
    cnt+=1
if cnt % 2 ==0:
    a = x
    b = cnt - x + 1
else:
    b = x
    a = cnt - x + 1
print(a,'/',b,sep='')