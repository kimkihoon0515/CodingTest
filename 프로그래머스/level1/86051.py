def solution(numbers):
    answer = 45
    sum = 0
    for i in numbers:
        sum += i
    answer -= sum
    return answer