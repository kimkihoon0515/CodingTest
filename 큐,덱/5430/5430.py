import sys
import re
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    p = list(map(str,sys.stdin.readline()))
    n = int(sys.stdin.readline())
    a = sys.stdin.readline()
    nums = re.findall("\d+",a)
    stack = deque(nums)
    for i in range(len(p)-1):
        if p[i] == 'R':
            stack.reverse()
        if p[i] == 'D':
            if len(stack) <1:
                print('error')
            else:
                stack.popleft()
    if len(stack) >0:
        print("[",end='')
        for i in range(len(stack)):
            if i == len(stack)-1:
                print(str(stack[i]),end='')
            else:
                print(stack[i],end=',')
        print("]")
    