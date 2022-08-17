def solution(A, B):
    answer = 0
    if min(A)>max(B):
        return 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    
    for i in range(len(A)):
        if A[i]<B[0]:
            B.pop(0)
            answer+=1
    
    return answer