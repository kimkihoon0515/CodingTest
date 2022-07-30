def solution(num):
    answer = 0
    while True:
        if num == 1 or answer == 500:
            break
        if num%2 == 0:
            num = num//2
        else:
            num = num*3 + 1
        answer +=1
    if num!= 1:
        answer = -1
    return answer