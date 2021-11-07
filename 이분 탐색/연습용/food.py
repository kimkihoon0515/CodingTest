import sys

n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort()

start = 1
end = li[-1]

while start <=end:
    mid = (start+end)//2
    sum = 0
    for i in li:
        if mid <= i:
            sum += (i-mid)
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)