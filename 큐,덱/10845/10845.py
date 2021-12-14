import sys

stack = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = list(sys.stdin.readline().split())
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if stack:            
            print(stack[-1])
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s[0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print(-1)