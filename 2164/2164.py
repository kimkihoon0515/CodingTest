from collections import deque
import sys

n = int(sys.stdin.readline()) # 1 ~ n 까지의 숫자범위

li = deque([i for i in range(n,0,-1)]) # 숫자들을 하나씩 배열에 반대로 넣어준다. 
cnt = 0 # 반복문을 돌리고 멈추기 위한 cnt
while (True):
    if n == 1: # 1개의 원소만 받으면 반복문을 나가고 1을 출력시킨다.
        break
    else: 
        li.pop() # 우선 먼저 배열의 가장 오른쪽원소를 삭제한다.
        li.insert(0,li[-1]) # 배열의 가장 왼쪽에다가 현재단계에서 가장 오른쪽 원소를 복사해온다.
        li.pop() # 배열의 가장 오른쪽 원소를 삭제하고 이 과정이 끝나면 cnt를 하나씩 올려준다. 
        cnt+=1 
    if cnt == (n-1): # 과정은 카드가 1장남을때까지 반복되는데 그것은 결국 처음에 입력한 숫자보다 하나 작게된다.
        break
print(li[0])

