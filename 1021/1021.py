import sys
from collections import deque

n,m  = map(int,sys.stdin.readline().split()) # stack을 채울 범위인 n과 그 중에서 m번째 원소를 받는다.

li=list(map(int,sys.stdin.readline().split())) # 출력할 원소를 집어넣은 배열이다.

stack = deque([i for i in range(1,n+1)]) # stack을 deque형식으로 선언한다.
cnt = 0

for i in li:
    while True:
        if stack[0] == i: # stack의 가장 첫번째 수와 li의 i가 같으면 반복문을 출력하고 다음번 li의 원소를 반복문돌린다.
            stack.popleft()
            break
        else:
            if stack.index(i) < len(stack)/2: # 만약 stack의 i번째가 왼쪽에서 더 가까울 경우에는 왼쪽으로 밀어준다.
                while stack[0] !=i:
                    stack.append(stack.popleft())
                    cnt+=1
            else: # 오른쪽에 더 가까운경우 오른쪽으로 밀어준다.
                while stack[0] != i:
                    stack.appendleft(stack.pop())
                    cnt +=1
print(cnt)
