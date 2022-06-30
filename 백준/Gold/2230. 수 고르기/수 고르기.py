import sys

n,m = map(int,sys.stdin.readline().split())

a = list(int(sys.stdin.readline().strip()) for i in range(n))
a.sort()

left = 0
right = 1
minimum = sys.maxsize

while left<n and right < n:
    minus = abs(a[left]-a[right])
    if minus == m:
        minimum = m
        break
    if minus < m:
        right +=1
        continue
    left +=1
    minimum = min(minimum,minus)
print(minimum)