import sys

n,m = map(int,sys.stdin.readline().split())
guitar = list(map(int,sys.stdin.readline().split()))

start = max(guitar)
end = sum(guitar)
ans = sys.maxsize

while start<=end:
    mid = (start+end)//2
    cnt = 0
    summary = 0
        
    for i in range(len(guitar)):
        if summary + guitar[i]>mid:
            summary = 0
            cnt+=1
        summary += guitar[i]
    if summary!=0:
        cnt +=1
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid-1

print(start)