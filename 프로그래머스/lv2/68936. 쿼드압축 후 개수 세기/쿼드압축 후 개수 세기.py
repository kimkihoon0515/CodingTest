def check(arr,s,n):
    x,y = s[0],s[1] # 각 arr의 왼쪽 상단
    target = arr[x][y]
    
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j]!=target:
                check(arr,[x,y],n//2)
                check(arr,[x+n//2,y],n//2)
                check(arr,[x,y+n//2],n//2)
                check(arr,[x+n//2,y+n//2],n//2)
                return
    answer[target]+=1

def solution(arr):
    global answer
    answer = [0,0]
    check(arr,answer,len(arr))
    return answer