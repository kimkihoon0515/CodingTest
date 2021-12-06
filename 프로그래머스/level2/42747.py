def solution(citations):
    answer = 0
    citations = sorted(citations)
    print(citations)
    for i,c in enumerate(citations):
        print(i,c)
        if c >= len(citations)-i:
            answer = len(citations)-i
            break
    return answer
print(solution([1,2,3,4,5,6,7]))