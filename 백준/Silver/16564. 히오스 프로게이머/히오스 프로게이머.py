import sys

n,k = map(int,sys.stdin.readline().split())
level = [int(sys.stdin.readline().strip()) for _ in range(n)]
level = sorted(level)

ans = -1

start = 1
end = level[-1]+k

while start <= end:
    mid = (start+end)//2
    summary = 0
    
    for i in range(len(level)):
        if level[i]<=mid:
            summary += mid-level[i]
    
    if summary <=k:
        start = mid+1
        ans = max(mid,ans)
    else:
        end = mid-1            

print(ans)