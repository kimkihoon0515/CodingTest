from collections import deque
import sys
from typing import Deque

while(True):
    li = Deque(list(map(int,sys.stdin.readline().split()))) # 히스토그램에 사용될 직사각형들의 높이를 입력받는다.
    n = li[0] # 첫 번째 원소를 저장해둘 변수. 
    answer = 0 # 직사각형의 넓이를 저장할 변수.
    stack = deque() # stack을 이용해서 높이가 가장 가장 마지막높이보다 작으면 지우고 아니면 추가하는 형식.
    if li[0] == 0:
        break
    else:
        li.popleft() # 맨 처음원소는 높이가아니고 직사각형의 개수이므로 지운다.
        for i in range(len(li)): 
            while len(stack) != 0 and li[stack[-1]] > li[i]: # stack이 비어있지 않고 가장 긴 높이보다 현재 높이가 작은 것이 들어오면
                tmp = stack.pop() # stack에서 가장 최근 원소를 지운다. 
                if len(stack) ==0: # 다 없어지면 높이는 너비는 i가 되고 
                    width = i
                else: # 그렇지 않으면 너비는 직사각형의 개수에서 stack에 저장되는 것은 몇 번째 사각형인지 그 번호이므로 그것을 지우고 -1을 해줘서 사이값을 구한다.
                    width = i - stack[-1]-1
                answer = max(answer,width * li[tmp]) # 그 값들 중 최대값을 answer로 넣어준다.
            stack.append(i)
    
        while len(stack) != 0:
            tmp = stack.pop() 
            if len(stack) ==0: #만약에 stack에 남아있는 원소가없다면 
                width = n # 너비는 직사각형들의 개수가 되고 높이는 stack에서 없어진 원소가 된다.
            else:
                width = n - stack[-1] -1
            answer = max(answer,width * li[tmp])
    print(answer) 


