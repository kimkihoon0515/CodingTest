import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)
print(sum(stack))