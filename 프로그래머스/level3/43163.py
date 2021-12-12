global answer
def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin] # 시작 단어
    while stacks:
        stack = stacks.pop() 
        if stack == target: # target과 같으면 answer를 return
            return answer
        
        for i in range(len(words)): # 차이나는 낱말이 1개이면
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:         
                if visit[i] ==0:
                    visit[i] = 1
                else:
                    continue
                stacks.append(words[i])
        answer += 1
    return answer

def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    return answer