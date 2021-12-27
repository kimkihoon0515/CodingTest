import sys

a,b = map(int,sys.stdin.readline().split())

num = [0]

for i in range(46): # 1000
    for j in range(i):
        num.append(i)

print(sum(num[a:b+1]))