import sys

n = int(sys.stdin.readline())

li = sorted(list(map(int,sys.stdin.readline().split())))

result = 0
cnt = 0
for i in li:
    cnt +=1
    if cnt >=i:
        result +=1
        cnt =0
print(result)