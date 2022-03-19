from itertools import permutations


def calculation(op,n,expression):
    if n == 2:
        return str(eval(expression)) # 최종 결과값
    if op[n] == '*': # 곱하기 경우
        return str(eval('*'.join([calculation(op,n+1,e) for e in expression.split('*')])))
    if op[n] == '+': # 덧셈 경우
        return str(eval('+'.join([calculation(op,n+1,e) for e in expression.split('+')])))
    if op[n] == '-': # 뺄셈 경우
        return str(eval('-'.join([calculation(op,n+1,e) for e in expression.split('-')])))


def solution(expression):
    answer = 0
    op = list(permutations(['+','-','*'],3)) # 우선순위 배열만들기
    for i in op:
        result = int(calculation(i,0,expression))
        answer = max(answer,abs(result)) # 절대값의 최대값 구하기
    return answer