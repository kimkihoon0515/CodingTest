def solution(n):
    answer = 0
    if n**(0.5) == int(n**(0.5)):
        answer = (int(n**0.5)+1)**2
    else:
        answer = -1
    return answer