import sys

queue = []

s = sys.stdin.readline().strip()

cnt = 0
for i in s:
    if i == '(': # 여는 괄호라면 
        queue.append(i) # queue에 넣는다.
    else: # 닫는 괄호일 경우
        if queue and queue[-1] == '(': # queue에 원소가 있고 마지막 원소가 여는 괄호라면
            queue.pop() # 여는 괄호를 없앨 수 있다.
        else: # queue가 비어져있을 경우
            cnt +=1 # cnt 하나 증가시킨다.

cnt += len(queue) # queue에 남은 원소만큼 괄호를 추가로 더해준다.
print(cnt)