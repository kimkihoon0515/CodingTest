# 내 풀이, hash table에 대해서 공부
def solution(participant, completion):
    answer = ''
    hash = {} # hash table 생성
    for i in participant:
        hash[i] = hash.get(i,0) + 1 # {'a':1,'b':2} 이런 식으로 만들어진다. 
    for i in completion: # completion에 있다면 hash value에서 -1 을 해서 결국 참가자 중에 완주를 못한 사람의 value만 1이 남게된다.
        hash[i] -= 1
    for i in hash:
        if hash[i]: # value가 1인 값을 answer에 대입해서 출력
            answer = i
    return answer

'''
베스트 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    collections.Counter를 통해 hash table이 만들어 진다. 참가자들의 hash table에서 완주자들의 hash table의 요소들을 빼준다.
    즉 한 사람의 이름과 value값인 1이 남게 된다. 결과값은 그 table의 0번째 요소인 이름을 출력
    return list(answer.keys())[0]
'''