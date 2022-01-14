import sys

x = sys.stdin.readline().strip()

y=0
cnt = 0
if len(x) >1:
    for i in x:
        y += int(i)
    cnt +=1
else:
    y = int(x)
    
while True:
    x = str(y)
    if y < 10:
        break
    y = 0
    for i in x:
        y += int(i)
    cnt +=1

print(cnt)
if y % 3 == 0 :
    print('YES')
else:
    print('NO')