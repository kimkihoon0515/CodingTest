import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s= sys.stdin.readline().strip()

p = 'I'
p = p + 'OI'*n
cnt = 0
result = 0
start = 1

while start <m-1:
    value = s[start-1:start+2]
    if value == 'IOI':
        cnt +=1
        if cnt == n:
            result +=1
            cnt -=1
        start +=1
    else:
        cnt = 0
    start +=1
print(result)