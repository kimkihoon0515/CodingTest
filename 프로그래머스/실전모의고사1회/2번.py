from collections import Counter

def solution(want, number, discount):
    answer = 0

    w = {}

    for i in range(len(want)):
        w[want[i]] = number[i]

    for start in range(len(discount)):
        flag = True
        end = start + 10
        if end>len(discount):
            end = len(discount)
        hash = Counter(discount[start:end])
        

        for key,value in w.items():
            if key not in hash:
                flag = False
                break

            else:
                if key in hash and value>hash[key]:
                    flag = False
                    break
        if flag:
            answer+=1

    return answer