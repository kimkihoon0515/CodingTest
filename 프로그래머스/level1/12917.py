def solution(s):
    answer = ''
    s = sorted(s,reverse = True) # 알파벳 역순으로 정렬 대문자는 뒤로 가게 된다.
    for i in s:
        answer += str(i)
    return answer