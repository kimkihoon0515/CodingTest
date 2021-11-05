import sys

n = int(sys.stdin.readline())

li = list(map(str,input().split()))
x = 0
y = 0
for i in li:
    if i == 'R':
        x += 1
    if i == 'U':
        y -= 1
        if y < 0:
            y = 0
    if i == 'L':
        x -= 1
        if x < 0:
            x = 0
    if i == 'D':
        y += 1
print(y+1,x+1)
