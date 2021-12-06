def solution(clothes):
    answer = 1
    hash = {}
    for n,t in clothes: # 옷에서 이름과 타입을 선택해서
        if t not in hash: # hash에 그 타입이 안들어가있으면
            hash[t] =1 # type : 1을 hash에 저장
        else:
            hash[t] +=1 # 이미 있다면 그 종류에서 +1을 함
    for v in hash.values(): # hash 의 value 값을 전부 곱해준다.
        answer *= (v+1)
    print(hash)
    return answer-1