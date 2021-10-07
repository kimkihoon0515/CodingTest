""" 시간초과 오류 발생 
n = int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(li[i])):
        if j == 0:
            li[i][j] = li[i][j]+ li[i-1][j]
        elif j == len(li[i])-1:
            li[i][j] = li[i][j] + li[i-1][j-1]
        else:
            li[i][j] = max(li[i-1][j-1],li[i-1][j]) + li[i][j]

print(max(li[n-1]))
"""

import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()[1:-1].split(',')
    stack = deque(a)
    reverse_flag = 0 # R이 짝수번 나오는지 홀수번 나오는지 검사하기위한 변수
    error_flag = 0 # error 가 나오는지 저장하기 위한 변수

    if n == 0:
        stack = [] 
    for i in p:
        if i == 'R':
            reverse_flag += 1
        if i == 'D':
            if len(stack) < 1:
                error_flag = 1
                print('error')
                break
            else:
                if reverse_flag % 2 == 0:
                    stack.popleft()
                else:
                    stack.pop()
    if error_flag == 0:
        if reverse_flag % 2 == 0:
            print('[' + ','.join(stack)+']')
        else:
            stack.reverse()
            print('['+','.join(stack)+']')