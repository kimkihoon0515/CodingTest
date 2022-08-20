import sys

n = int(sys.stdin.readline())
u = [int(sys.stdin.readline().strip()) for _ in range(n)]

summary = set()

for i in u:
    for j in u:
        summary.add(i+j)

ans = set()
for i in u:
    for j in u:
        if i-j in summary:
            ans.add(i)

print(max(ans))  