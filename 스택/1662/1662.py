import sys

s = sys.stdin.readline().strip()    
stack = []

'''
1 3 (2 2(1 1 (1)))
1 3 (2 2 (1 1))
1 3 (2 2 (2))
1 3 (2 4)
1 3 (6)
1 18
19
'''

for i in range(len(s)):
    if i < len(s) -1 and s[i+1] == '(': # (로 열리면 바로 다음문자를 stack에 넣는다.
        stack.append(s[i])
    elif s[i] == '(': 
        stack.append(s[i])
    elif s[i] == ')':
        cnt = 0
        while True:
            tmp = stack.pop()
            if tmp == '(':
                break
            cnt += tmp # 괄호 안의 숫자들을 전부 더한다.
        stack.append(int(stack.pop()) * cnt) # 괄호안의 모든 값과 바로 왼쪽의 숫자를 곱해서 다시 stack에 쌓는다.
    else: # 그 외의 숫자들은 전부 1로 치환
        stack.append(1)

print(sum(stack))