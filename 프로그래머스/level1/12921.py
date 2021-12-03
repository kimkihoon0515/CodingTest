def prime(n): # 에라토스테네스의 체를 이용한 소수 구하기
    arr = [True for i in range(n+1)]
    
    m = int(n**0.5)
    for i in range(2,m+1):
        if arr[i] == True:
            for j in range(i+i,n+1,i): # i 이후의 i의 배수들을 전부 False로 만듬
                arr[j] = False
    
    cnt = 0 # 소수의 개수 구하기
    for i in range(2,len(arr)): 
        if arr[i] == True: # 소수라면 개수 1씩 증가
            cnt +=1
            
    return cnt 
    
def solution(n):
    answer = prime(n)
    return answer
