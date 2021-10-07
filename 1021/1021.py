import sys
from collections import deque

n,m  = map(int,sys.stdin.readline().split())

li=list(map(int,sys.stdin.readline().split()))

stack = deque([i for i in range(1,n+1)])
cnt = 0

for i in li:
    while True:
        if stack[0] == i:
            stack.popleft()
            break
        else:
            if stack.index(i) < len(stack)/2:
                while stack[0] !=i:
                    stack.append(stack.popleft())
                    cnt+=1
            else:
                while stack[0] != i:
                    stack.appendleft(stack.pop())
                    cnt +=1
print(cnt)
