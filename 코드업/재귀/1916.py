import sys
sys.setrecursionlimit(10000000)
n = int(sys.stdin.readline().strip())

dic = {0:0,1:1}

def fib(n):
    if n in dic:
        return dic[n]
    dic[n] = fib(n-1)+fib(n-2)
    return dic[n]%10009

print(fib(n))