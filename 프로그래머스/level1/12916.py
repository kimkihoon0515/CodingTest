# 내 풀이 
def solution(s):
    answer = True
    p_cnt = 0 # p의 개수
    y_cnt = 0 # y의 개수 
    for i in s:
        if i == 'p' or i == 'P': 
            p_cnt +=1
        elif i == 'y' or i == 'Y':
            y_cnt +=1
    if p_cnt == y_cnt: # 각각 구해서 개수 비교함.
        return True
    return False

'''
베스트 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y') # lower를 통해 모든 문자를 소문자로 바꾸고 count를 통해 개수를 반환

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
'''