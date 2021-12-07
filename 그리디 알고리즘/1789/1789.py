import sys

s = int(sys.stdin.readline().strip())
cnt = 0
while (cnt*(cnt+1))/2<=s:
    cnt+=1
print(cnt-1)