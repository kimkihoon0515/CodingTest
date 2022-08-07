def solution(s):
    answer = 1
    n = len(s)
    
    for start in range(n):
        end = start+1
        while end < n:
            l = s[start:end+1]
            if l == l[::-1]:
                answer = max(answer,len(l))
            end+=1
    return answer