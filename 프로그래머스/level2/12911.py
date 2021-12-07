def bin(n):
    ans = format(n,'b') # 이진수로 변환
    return ans.count('1') # 1의 개수 count
def solution(n):
    answer = n+1 
    while bin(answer)!=bin(n): # 조건을 만족하는 가장 작은 수를 찾기위해
        answer +=1
    return answer