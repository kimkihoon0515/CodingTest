import sys

a,b = map(int,sys.stdin.readline().split())
a_list = [0,a]
b_list = [0,b]

n = int(sys.stdin.readline())

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x == 0:
        b_list.append(y)
    else:
        a_list.append(y)

a_list.sort()
b_list.sort()

answer = -1
for i in range(1,len(a_list)):
    for j in range(1,len(b_list)):
        w = a_list[i]-a_list[i-1]
        h = b_list[j]-b_list[j-1]
        answer = max(answer,w*h)

print(answer)