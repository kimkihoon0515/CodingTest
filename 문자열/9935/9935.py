''' 시간초과 오류 뜸 ㅠ
import sys

s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

while True:
    if bomb not in s:
        break
    else:
        s = s.replace(bomb,'')

if len(s) == 0:
    print('FRULA')
else:
    print(s)
'''
import sys

s = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())

stack = []
for i in s:
    stack.append(i)
    if i == bomb[-1]: # stack의 마지막 원소와 폭탄의 마지막원소가 같으면
        if stack[-len(bomb):] == bomb: # stack의 마지막원소로부터 거꾸로 확인을 해서 폭탄과 같으면
            for j in range(len(bomb)): # 폭탄의 길이만큼 stack에서 pop한다.
                stack.pop()

if len(stack) == 0: # 전부 없어지면 
    print('FRULA')
else:
    print(''.join(stack)) # 결과값 출력
    