import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

end = 0 

ans = sys.maxsize
result = 0
prev = 0

for start in range(n):
    summary = li[start]
    end = start+1
    while end < n:
        summary += li[end]
        prev = ans
        ans = min(ans,abs(summary))
        if ans!=prev:
            result = summary
        if ans == 0:
            break
        else:
            summary = li[start]
            end +=1


print(result)