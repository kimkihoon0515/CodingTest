import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    stack = [s[0]] # 시작점을 스택에 넣고
    for i in s[1:]: # 반복문돌려서 같은것이 들어오지않으면 stack에 계속 넣는 방향으로 진행
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) ==0:
        cnt +=1
print(cnt)