# 풀이 참고했음. 봐도 잘 모르겠어서 다시 확인해봐야할듯?
def solution(n, cores):
    answer = 0
    if n <len(cores):
        return n
    
    n-=len(cores)
    left = 1
    right = max(cores)*n
    
    while left<right:
        mid = (left+right)//2
        tmp = 0
        for core in cores:
            tmp += mid//core
        if tmp >=n:
            right = mid
        else:
            left = mid+1
    
    for core in cores:
        n-=(right-1)//core
    
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n-=1
            if n == 0:
                return i+1
        
        