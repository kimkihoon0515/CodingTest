import math
def solution(enroll, referral, seller, amount):
    answer = []
    sell = dict()
    reference = dict()

    for i in range(len(enroll)):
        sell[enroll[i]] = 0
        reference[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        money = amount[i]*100
        s = seller[i]
        while s!='-':
            sell[s] += math.ceil(money*0.9)
            money -= math.ceil(money*0.9)
            if money == 0:
                break
            s = reference[s]
    for key,value in sell.items():
        answer.append(value)
    return answer