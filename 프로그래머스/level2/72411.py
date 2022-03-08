from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    li = []
    for i in course:
        for j in orders:
            comb = combinations(sorted(j),i) # 손님이 주문할 수 있는 조합
            li+=comb # 모든 손님이 주문할 수 있는 조합의 배열
    dic = Counter(li) # 모든 조합이 각각 얼마나 겹치는지 나타내는 dic 형태
    #print(dic)
    for v,k in sorted(dic.items(),key=lambda x:x[1],reverse=True):
        if not answer and k > 1: # 코스요리는 최소 2번이상 주문되어야 가능하고 주문횟수로 정렬했으므로 answer 배열이 비어있으면 무조건 넣는다.
            answer.append([''.join(v),k])
        else:
            if len(answer[-1][0]) == len(v) and k == answer[-1][1]: # 코스요리의 알파벳 길이가 같으면서 주문횟수도 같은 경우
                answer.append([''.join(v),k])
            elif len(answer[-1][0]) < len(v) and k > 1: # 코스요리의 알파벳 길이가 길어지고 주문횟수가 2번이상이면
                answer.append([''.join(v),k])
    result = []
    for v,k in answer:
        result.append(v)
    result = sorted(result) # 주문횟수별로 정렬되어 들어갔기 때문에 다시 알파벳순으로 정렬해준다
    return result