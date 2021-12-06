''' 시간초과 나는 풀이
from itertools import combinations
def solution(number, k):
    answer = ''
    result = sorted(list(map(''.join,list(combinations(number,len(number)-k)))))
    return result[-1]
'''
# 정답풀이
def solution(number, k):
    stack = []
    stack.append(number[0]) # 첫 번째 수를 선택한 것으로 생각하고 
    for i in number[1:]: # 그 다음숫자부터 반복문돌림
        while stack and int(i) > int(stack[-1]) and k > 0: # 새로 들어오려는 숫자가 현재 들어있는 가장 바깥 숫자보다 크면 기존 숫자를 없앤다.
            stack.pop()
            k-=1 # k 하나 감소
        stack.append(i) # i를 stack에 넣어준다. 
        if len(stack) == len(number) - k:
            break
    answer = ''.join(stack)
    return answer
