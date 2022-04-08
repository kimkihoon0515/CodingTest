import sys

t = int(sys.stdin.readline().strip())

K = [int(sys.stdin.readline().strip()) for i in range(t)]


li = [n*(n+1)//2 for n in range(1,46)]

ans = [0 for i in range(1001)]

for i in li:
    for j in li:
        for k in li:
            if i+j+k <= 1000:
                ans[i+j+k] = 1
                

for i in K:
    print(ans[i])