def solution(a, b, n):
    answer = 0

    rest,new = divmod(n,a)
    while True:
        if n<a:
            break
        
        rest,new = divmod(n,a)
        rest = rest*b
        answer += rest
        n = rest+new


    return answer