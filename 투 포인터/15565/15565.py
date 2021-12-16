import sys

n,k = map(int,sys.stdin.readline().split())

doll = list(map(int,sys.stdin.readline().split()))

result = len(doll)

if doll.count(1) < k:
    print(-1)
    exit()
else:
    for start in range(len(doll)):
        end = start
        cnt = 0
        while end < len(doll) :
            if doll[end] == 1:
                cnt +=1
            if cnt == k:
                result = min(result,end-start+1)
                break
            end +=1
print(result)

        
                 