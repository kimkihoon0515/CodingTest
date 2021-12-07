answer = 0
def dfs(numbers,target,index,s):
    global answer
    if len(numbers) == index: # 배열의 마지막 원소까지 돌렸고 
        if target == s: # 총 합이 target과 같으면
            answer +=1 # answer 1 증가
        return
    dfs(numbers,target,index+1,s+numbers[index]) # 재귀로 풀이, 총 합에 + 한 것과 - 한 것 나눠서 돌림
    dfs(numbers,target,index+1,s-numbers[index])
    
def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0) # 초기 dfs
    return answer