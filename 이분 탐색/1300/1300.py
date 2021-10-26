import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
"""
123 
246
369 
"""
start = 1
end = k

while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in range(1,n+1):
        sum += min(mid//i,n) # mid 이하의 i의 배수이거나 아니면 최대 n
    if sum >=k:
        answer = mid
        end = mid -1
    else:
        start = mid +1

print(answer)