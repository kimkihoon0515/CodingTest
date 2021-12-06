def solution(A,B):
    answer = 0
    a = list(sorted(A,reverse = True)) # 역순정렬
    b = list(sorted(B)) # 정렬
    for i in range(len(a)): # 순서대로 곱해서 더해준다.
        answer += a[i] * b[i]
    return answer