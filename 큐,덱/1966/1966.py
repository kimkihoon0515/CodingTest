import sys
from collections import deque

t = int(sys.stdin.readline())


for _ in range(t):
    n,m = map(int,sys.stdin.readline().split()) # 문서의 개수 n, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 queue에서 몇 번째에 놓여있는지 m
    li = deque(map(int,sys.stdin.readline().split()))
    result = deque(i for i in range(n)) # 인덱스 저장을 위한 배열
    cnt = 0 # 몇 번째로 출력되었는지
    while li:
        if li[0] == max(li): # 만약 첫원소가 가장 우선순위가 높으면
            cnt +=1 # cnt를 하나증가시키고 제거한다. 그리고 만약 그것이 m값과 동일하면 출력한다.
            li.popleft()
            if result.popleft() == m:
                print(cnt)
        else: # 그렇지 않으면 제거하고 가장 오른쪽에 추가해준다.
            li.append(li.popleft()) 
            result.append(result.popleft()) 