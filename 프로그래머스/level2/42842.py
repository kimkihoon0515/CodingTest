def solution(brown, yellow):
    answer = []
    sum = brown+yellow
    a = 0
    b = 0
    while True:
        b +=1
        a = yellow/b
        if yellow%b !=0:
            continue
        elif (a+2)*(b+2) == sum:
            answer = [a+2,b+2]
            break
    return answer