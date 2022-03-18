def solution(s):
    answer = 0
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for index,values in enumerate(numbers):
        if values in s:
            s = s.replace(values,str(index)) # 영어를 숫자로 변환
    answer = int(s) # type을 int형으로 변경
    return answer