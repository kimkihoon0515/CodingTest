import sys

n = int(sys.stdin.readline().strip())

tower = list(map(int,sys.stdin.readline().split()))

stack = []

ans = []

for i in range(len(tower)):
    while stack:
        if stack[-1][1]>tower[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i,tower[i]])
print(*ans)