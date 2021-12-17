import sys

n,k = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0

counter = [0 for i in range(max(li)+1)]

cnt = 0

while end < n:
    if counter[li[end]] < k:
        counter[li[end]] += 1
        end +=1
    else:
        counter[li[start]] -= 1
        start +=1
    cnt = max(cnt,end-start)
print(cnt)       
    