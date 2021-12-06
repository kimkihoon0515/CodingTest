def fib(n):
    a = [0 for i in range(n)]
    a[0] = 0
    a[1] = 1
    a[2] = 2
    for i in range(3,n):
        a[i] = (a[i-1]+a[i-2]) %1234567 # 먼저 나눠주어야 시간초과안걸림
    
    return a[-1]
    

def solution(n):
    answer = 0
    print(n)
    answer = fib(n)
    return answer