import sys

n,m = map(int,sys.stdin.readline().split())

t = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = 0
right = max(t)*m

while left <= right:
    mid = (left+right)//2
    people = sum(mid//i for i in t)
    if people >= m :
        answer = mid
        right = mid-1
    else:
        left = mid +1
print(answer)