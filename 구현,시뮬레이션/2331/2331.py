import sys

a,p = map(str,sys.stdin.readline().split())

li = [int(a)]

while True:
    s = 0
    for i in range(len(a)):
        s += int(a[i])**int(p)
    if s in li:
        break
    else:
        li.append(s)
    a = str(s)
    
print(li.index(s))