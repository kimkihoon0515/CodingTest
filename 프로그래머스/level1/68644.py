import itertools
def solution(numbers):
    answer = []
    per = list(itertools.combinations(numbers,2))
    result = []
    for i in per:
        s = 0
        s += sum(i)
        result.append(s)
    result.sort()
    for value in result:
        if value not in answer:
            answer.append(value)
    return answer