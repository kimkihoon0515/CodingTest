def solution(strings, n):
    result = sorted(strings) # 우선 사전 순으로 정렬한다.
    answer = sorted(result,key=lambda x: x[n]) # 사전순으로 정렬한 것을 n번째 알파벳을 기준으로 다시 정렬한다.
    return answer