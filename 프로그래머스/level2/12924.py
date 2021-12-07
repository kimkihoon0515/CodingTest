# 내 풀이(시간초과 발생 )
def solution(n):
    answer = 1
    arr = [i for i in range(n+1)] # 처음부터 arr를 만들어놓고 돌릴 경우 n번 계속 탐색하게 되어 시간초과발생하는듯
    print(arr)
    for i in range(1,n//2+1):
        sum = 0
        for j in range(i,n+1):
            sum += arr[j]
            if sum == n:
                answer +=1
    return answer

# 정답 풀이
def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        stack = [] 
        for j in range(i, n + 1):
            stack.append(j) # i부터 차례대로 stack에 넣어주고 
            if sum(stack) >= n: # 그 합이 n이되면
                break # 종료
        if sum(stack) == n:
            answer += 1

    return answer