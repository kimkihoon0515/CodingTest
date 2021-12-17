import sys

n,k = map(int,sys.stdin.readline().split())

doll = list(map(int,sys.stdin.readline().split()))


if doll.count(1) < k:
    print(-1)
    exit()
else:
    lion = [k for k,v in enumerate (doll) if v == 1]
    result = sys.maxsize
    start = 0
    end = k-1
    while True:
        result = min(result,lion[end]-lion[start]+1)
        if end == len(lion)-1:
            break
        start+=1
        end +=1
print(result)