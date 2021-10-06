from collections import deque

n, k = map(int, input().split()) # n과 k를 입력받는다.

li = deque([i for i in range(1,n+1)]) # 1 ~ n까지의 숫자를 입력한다.

result = [] # 결과값이 들어갈 배열이다.

while li: # 1~ n까지 돌면서 전부 다 없어질 때까지 반복한다.
    for i in range(k-1): # k 전까지의 모든 요소들을 없애서 새로 넣어준다. 그리고 결과배열에는 k를 넣어준다. 그런식으로 계속 반복한다.
        li.append(li.popleft())
    result.append(li.popleft())

print("<",end='') # 형식에 맞게 출력한다.
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")
