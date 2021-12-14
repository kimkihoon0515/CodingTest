def solution(s):
    answer = -1
    stack = [s[0]] # 문자열 맨 처음 글자 넣고
    
    for i in range(1,len(s)): # 반복문돌려서
        if stack and stack[-1] == s[i]: # stack에 글자가 있고 마지막 글자가 같으면
            stack.pop() # 없애고
        else: # 아니면 넣는다.
            stack.append(s[i]) 
    if not stack: # stack이 비어있으면 1 아니면 0을 출력
        answer = 1
    else:
        answer = 0
    return answer