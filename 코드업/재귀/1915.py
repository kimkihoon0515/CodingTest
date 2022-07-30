import sys

sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().strip())

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(n))