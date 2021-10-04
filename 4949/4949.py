import sys
while (True): 
    s = list(map(str,sys.stdin.readline())) # 문자열을 입력받는다.
    li = [] # 균형잡혀있는지 아닌지 구별하기 위해 잠시 저장하는 배열
    if s[0] == '.': # .을 입력받을 때까지 반복문을 돌린다.
        break
    else:
        for i in s: 
            if i == '(' or i == '[': # 두 개의 열리는 괄호가 있으면 배열에 저장한다.
                li.append(i)
            elif i == ']': # 대괄호 닫는 것이 오면 배열에 원소가 들어가있고 마지막 원소가 [ 라면 배열에서 제거한다.
                if len(li) !=0 and li[-1] == '[':
                    li.pop()
                else: # 만약 ] 가 아니면 다시 배열에 넣어주고 반복문을 나간다. 이 경우에는 no를 출력하게 된다. 
                    li.append(i)
                    break
            elif i == ')': # 만약 소괄호 닫는 것이 오면 배열에 원소가 들어가 있고 마지막 원소가 ( 라면 배열에서 제거한다.
                if len(li) !=0 and li[-1] == '(': 
                    li.pop()
                else: # 그렇지 않다면 배열에 저장하고 반복문을 종료한다. 이 경우에도 마찬가지로 no를 출력하게 된다.
                    li.append(i)
                    break
        if len(li) == 0: # 배열의 요소가 전부 제거되면 균형잡힌 문자열이므로 yes를 출력하고 아니면 no를 출력한다.
            print('yes')
        else:
            print('no')