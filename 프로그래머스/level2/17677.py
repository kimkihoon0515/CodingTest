import math

def jakad(s): # 자카드 유사도 구하는 함수
    result = []
    for i in range(len(s)-1):
        word = s[i]+s[i+1]
        if word.isalpha(): # 알파벳만 
            result.append(word) # 배열에 넣는다.
    return result

def solution(str1, str2):
    answer = 0
    str1 = str1.lower() # 대문자,소문자 구별없이
    str2 = str2.lower()
    
    str1 = jakad(str1)
    str2 = jakad(str2)
    
    print(str1,str2)

    intersect = set(str1) & set(str2) # 교집합
    union = set(str1) | set(str2) # 합집합

    if len(union) == 0 :
        return 65536

    cross_sum = sum([min(str1.count(i), str2.count(i)) for i in intersect]) # 교집합의 원소 개수
    union_sum = sum([max(str1.count(i), str2.count(i)) for i in union])  # 합집합의 원소 개수
    answer = math.floor((cross_sum/union_sum)*65536)
    return answer