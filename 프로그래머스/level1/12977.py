from itertools import combinations

def prime(a): # 소수 판별 
    x = sum(a)
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    # [1,2,3,4] 중 3개 골라서 소수
    answer = 0
    
    result = list(combinations(nums,3))
    
    for i in result:
        if prime(i):
            answer += 1
    
    return answer