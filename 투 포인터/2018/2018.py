import sys

n = int(sys.stdin.readline())
li = [i for i in range(1,n+1)]

result = 0
sum = 0
end = 0

for start in range(n):
    while sum < n and end < n:
        sum += li[end]
        end +=1
    if sum == n:
        result += 1
    sum -= li[start]
print(result)