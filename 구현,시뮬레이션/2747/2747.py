import sys

n = int(sys.stdin.readline())

def fib(n):
    ans = [1,1]
    for i in range(2,n):
        answer = ans[i-2]+ans[i-1]
        ans.append(answer)
    return ans[-1]

print(fib(n))