def solution(s):
    answer = ''
    a = list(s)
    c = 0
    for i in range(len(s)):
        if a[i].isalpha and c % 2 == 0 and a[i].islower():
            answer += a[i].upper()
            c += 1
        elif a[i].isalpha and c % 2 == 0 and a[i].isupper():
            answer += a[i]
            c += 1
        elif a[i] == ' ':
            c = 0
            answer += ' '
        elif c % 2 == 1 and a[i].isupper():
            answer += a[i].lower()
            c += 1
        elif c % 2 == 1 and a[i].islower():
            c += 1
            answer += a[i]
    return answer