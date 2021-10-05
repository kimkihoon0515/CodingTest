import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = list(sys.stdin.readline().rstrip('\n').split(' '))
    if command[0]=='push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])