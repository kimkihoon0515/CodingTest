import sys

s = sys.stdin.readline().strip()    

def check(s):
    stack = []
    flag = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[': # 왼쪽괄호면 stack에 넣고
            stack.append(s[i])
        else: # 그게 아니면 
            if s[i] == ')': # 동그란 괄호이고
                if stack and stack[-1] == '(': # stack이 비어있지 않고 마지막 원소가 왼쪽동그란괄호면
                    stack.pop() # 왼쪽동그란괄호를 없앤다.
                else: # stack이 비어있거나 즉 처음 들어가는 것이 ] 이거나 아니면 마지막 원소가 ( 라면 
                    flag = False # flag를 False로 바꾼다.
             
            else: # 네모난 괄호라면
                if stack and stack[-1] == '[': # 위의 조건과 동일
                    stack.pop()
                else:
                    flag = False
    if not stack and flag: # stack이 모두 없어졌고 flag가 True면
        return True  
    return False # 그 외에는 전부

def cal(s):
    stack=[]
    
    for i in range(len(s)): # check와 동일하게 넣어준다.
        if s[i]== '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')': 
                if stack[-1] == '(': # 만약 stack의 마지막 원소가 왼쪽 동그란괄호면
                    stack[-1] = 2 # 그것을 숫자 2로 바꿔준다.
                else: # 그렇지 않다면
                    tmp = 0 # 숫자들의 합을 계산하기 위한 변수
                    for j in range(len(stack)-1,-1,-1): # 역순으로 찾는다.
                        if stack[j] == '(': # 괄호를 발견하면
                            stack[-1] = tmp*2 # (x)는 x 에다가 *2를 해준다.
                            break
                        else: # 숫자가 계속 나온다면
                            tmp +=stack[-1] # 숫자를 누적합으로 계산한다.
                            stack.pop() # 계산된 숫자들은 전부 stack에서 없애준다.
            else: # ] 가 들어오려할때 
                if stack[-1] == '[': # 마지막 원소가 왼쪽 네모난 괄호면
                    stack[-1] = 3 # 3으로 바꿔준다.
                else: # 괄호가 완성되지않으면
                    tmp = 0 # 누적합을 구하기 위한 변수
                    for j in range(len(stack)-1,-1,-1): # 역순으로 찾는다.
                        if stack[j] == '[': # 만약 괄호를 찾았다면
                            stack[-1] = tmp*3 # [x] 는 x에다가 *3을 해준다.
                            break
                        else: # 숫자가 계속 나온다면
                            tmp += stack[-1] # 숫자를 누적합으로 계산한다.
                            stack.pop() # 계산된 숫자들은 없애준다.
    return sum(stack) # 모든 괄호의 계산값

if check(s):
    print(cal(s))
else:
    print(0) 