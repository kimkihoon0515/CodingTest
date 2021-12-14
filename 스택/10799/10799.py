import sys

s = sys.stdin.readline().strip()

stack = []
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':
            stack.pop()
            answer += len(stack) # 쇠막대기의 개수만큼 더해주고
        else:
            stack.pop()
            answer +=1 # 쇠막대기 끄트머리 부분이니까 하나씩 더해준다.
print(answer)