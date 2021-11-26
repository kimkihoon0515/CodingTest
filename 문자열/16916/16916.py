import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

def maketable(tmp): # 테이블 만드는 과정
    lp = len(tmp)
    i = 0
    table = [0] * lp
    for j in range(1,lp):
        while i > 0 and tmp[i] != tmp[j]: # 모든 문자를 하나씩 검사해서  i번째 문자와 j번째 문자가 일치하지 않으면
            i = table[i-1] # i를 table의 i-1 인덱스로 변경
        if tmp[i] == tmp[j]: # 일치한다면
            i += 1 # i만 하나씩 증가시킨다.
            table[j] = i 
    return table

def kmp(string,pattern): 
    table = maketable(pattern) # 패턴테이블을 만든다.
    i = 0
    for j in range(len(string)): # s 만큼 반복문을 돌린다.
        while i > 0 and string[j] != pattern[i]: # i와 j가 같지 않으면
            i = table[i-1] # i를 table의 i-1 인덱스로 옮긴다.
        if string[j] == pattern[i]: # p의 부분 수열이 s에 포함이 되는경우
            if i == len(pattern)-1: # i가 p의 길이-1과 같은 경우
                return 1 # 1을 리턴하고
            else: # 아니면 i를 하나 늘려서 p의 길이를 늘려간다.
                i += 1
    return 0

print(kmp(s,p))
#print(maketable(p))        