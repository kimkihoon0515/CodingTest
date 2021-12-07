def solution(s):
    answer = ''
    li = s.lower().split(' ')
    print(li)
    for i in range(len(li)):
        li[i] = li[i][:1].upper() + li[i][1:].lower()
    answer = ' '.join(li)
    return answer