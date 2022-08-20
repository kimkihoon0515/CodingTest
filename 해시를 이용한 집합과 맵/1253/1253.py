import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
# n개의 수 중 어떤 수가 다른 수 두개의 합으로 나타낼 수 있다면 GOOD라고 한다.
a = sorted(a)
cnt = 0

for start in range(n):
    li = a[:start]+a[start+1:]
    left = 0
    right = n-2
    while left<right:
        summary = li[left]+li[right]
        if summary == a[start]:
            cnt+=1
            break
        if summary > a[start]:
            right -=1
        else:
            left +=1
print(cnt)