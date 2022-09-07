import sys

n = int(sys.stdin.readline())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

li.sort()
ans = 0
left = li[0][0]
right = li[0][1]

for i in range(1,n):
    if li[i][0] <= right and right < li[i][1]:
        right = li[i][1]
    if right < li[i][0]:
        ans = ans + right - left
        left = li[i][0]
        right = li[i][1]

ans = ans + right - left
print(ans)