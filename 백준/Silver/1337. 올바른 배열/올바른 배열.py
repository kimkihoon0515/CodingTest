import sys

n = int(sys.stdin.readline())

li = [int(sys.stdin.readline().strip()) for _ in range(n)]

ans = 5

for i in range(n):
    cnt1 = 4
    cnt2 = 4
    for j in range(n):
        if li[i]+5>li[j] and li[i]<li[j]:
            cnt1-=1
        if li[i]-5 < li[j] and li[i]>li[j]:
            cnt2-=1
    ans = min(ans,cnt1,cnt2)
print(ans)