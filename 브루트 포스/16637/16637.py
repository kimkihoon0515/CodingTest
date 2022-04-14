import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def calculate(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '*':
        return a*b
    elif operator == '-':
        return a-b
    
num = []
op = []

for i in s:
    if i.isdigit(): # 숫자만으로 이루어진 배열 생성
        num.append(int(i))
    else: # 연산자만으로 이루어진 배열 생성
        op.append(i)

def dfs(index,ans):
    global maximum
    if index >= len(op): # 모든 연산자를 다 사용했다면
        maximum = max(maximum,ans)
        return
    
    dfs(index+1,calculate(ans,num[index+1],op[index])) # 계산이 가능한 경우
     
    if index + 1 < len(op): # 괄호가 닫혀있지 않아서 연산이 불가능한경우
        dfs(index+2, calculate(ans, calculate(num[index+1], num[index+2], op[index+1]), op[index]))        
        

maximum = -9999999999
dfs(0,num[0])
print(maximum)


