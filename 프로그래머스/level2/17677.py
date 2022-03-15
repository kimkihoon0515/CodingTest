import math

def jakad(s):
    result = []
    for i in range(len(s)-1):
        word = s[i]+s[i+1]
        if word.isalpha():
            result.append(word)
    return result

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = jakad(str1)
    str2 = jakad(str2)
    
    print(str1,str2)

    intersect = set(str1) & set(str2)
    union = set(str1) | set(str2)

    if len(union) == 0 :
        return 65536

    cross_sum = sum([min(str1.count(i), str2.count(i)) for i in intersect])
    union_sum = sum([max(str1.count(i), str2.count(i)) for i in union])
    answer = math.floor((cross_sum/union_sum)*65536)
    return answer