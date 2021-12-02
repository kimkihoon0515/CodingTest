def solution(d, budget):
    #[1,3,2,5,4],9 -> 3
    answer = 0
    d.sort()
    cnt = 0
    for i in d:
        if i <= budget:
            cnt +=1
            budget -=i
        else:
            break
    return cnt