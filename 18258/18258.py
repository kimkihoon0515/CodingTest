import sys
from typing import Deque
n = int(sys.stdin.readline())


li = Deque([]) # deque를 사용하지 않을 경우 가장 처음원소를 지울 때 지우고 다시 넣기 때문에 시간초과가 난다. 
s = []
for i in range(n):
    s = list(map(str,sys.stdin.readline().split()))
    if len(s) == 1:
        if s[0] == 'back':
            if len(li) > 0:
                print(li[len(li)-1])
            else:
                print(-1)
        if s[0] == 'front':
            if len(li) > 0:
                print(li[0])
            else:
                print(-1)
        if s[0] == 'size':
            print(len(li))
        if s[0] == 'pop': # 파이썬의 list 를 가장 앞 데이터를 지울 경우 두번째 원소부터 다시 새로 작성을 하기 때문에 deque로 구현하고 popleft함수를 사용해서 시간복잡도를 낮춘다.
            if len(li) > 0:
                print(li.popleft())
            else:
                print(-1)
        if s[0] == 'empty':
            if len(li) == 0:
                print(1)
            else:
                print(0)
    else:
        li.append(s[1])
