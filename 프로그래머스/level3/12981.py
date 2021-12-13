def solution(n, words):
    answer = [0,0]
    
    b = words[0][-1] # 마지막 글자
    for i in range(1,len(words)): 
        if words[i][0] != b or words[i] in words[:i]: # 끝말잇기 조건이 성립이 안되면
            a,b = divmod(i,n) # 몫과 나머지
            answer[1] = a+1 # 몇 번째로 말한 단어
            answer[0] = b+1 # 몇 번째사람이
            break
        else: # 끝말잇기가 성립이 된다면
            b = words[i][-1] # 마지막 단어를 갱신
    return answer