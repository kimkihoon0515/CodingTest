def fib(n):
    ans = [0 for i in range(n+1)]
    ans[1] = 1
    ans[2] = 2
    for i in range(3,n+1):
        ans[i] = (ans[i-1]+ans[i-2])%1000000007
    return ans[-1]
def solution(n):
    answer = 0
    answer = fib(n)
    return answer