def solution(numbers, target):
    answer = 0
    def dfs(result,idx):
        nonlocal answer
        if idx == len(numbers):
            if result == target:
                answer+=1
            return
        dfs(result+numbers[idx],idx+1)
        dfs(result-numbers[idx],idx+1)

    dfs(0,0)

    return answer