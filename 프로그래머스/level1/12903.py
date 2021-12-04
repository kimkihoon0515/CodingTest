def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        n = len(s) // 2
        answer = answer + s[n-1] + s[n]
    else:
        n = len(s) // 2 + 1
        answer = answer + s[n-1]
    
    return answer