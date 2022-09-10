import sys

n = int(sys.stdin.readline())
left = 1
right = n

while left<=right:
    mid = (left+right)//2
    if mid**2 == n:
        break
    if mid**2 > n:
        right = mid - 1
    else:
        left = mid + 1

print(mid)