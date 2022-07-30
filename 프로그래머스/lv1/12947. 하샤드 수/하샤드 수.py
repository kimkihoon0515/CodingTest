def solution(x):
    answer = True
    s = str(x)
    a = 0
    for i in range(len(s)):
        a+=int(s[i])
    if x % a !=0:
        answer = False
    return answer