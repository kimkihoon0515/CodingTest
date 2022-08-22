from collections import Counter

def solution(topping):
    answer = 0

    hash = Counter(topping)
    
    dic = {}

    for i in range(len(topping)):
        if topping[i] in hash and hash[topping[i]]>0:
            hash[topping[i]] -= 1
            if hash[topping[i]] == 0:
                del hash[topping[i]]
            if topping[i] not in dic:
                dic[topping[i]] = 1
            else:
                dic[topping[i]]+=1
        
        if len(hash) == len(dic):
            answer+=1



    return answer