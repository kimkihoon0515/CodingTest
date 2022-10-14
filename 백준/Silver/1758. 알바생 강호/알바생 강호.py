import sys

n = int(sys.stdin.readline().strip())

li = []
ans = 0

for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort(reverse=True)

for i in range(n):
    result = li[i]-i

    if result>0:
        ans+=result

print(ans)