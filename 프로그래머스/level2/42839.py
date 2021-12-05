from itertools import permutations

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    li = []
    result = []
    for i in range(1,len(numbers)+1):
        li = list(map(''.join,permutations(numbers,i))) # 글자들을 조합하여 li에 배열의 형태로 저장
        li = set(li) # 중복되는것 제거
        for i in li:
            if prime(int(i)) == True: # 소수이면
                result.append(int(i)) # 결과배열에 우선 넣어놓고
        
    answer = len(set(result)) # 중복되는 결과 제거 ex) 011,11 
    return answer