import sys

sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())

def func(n):
    if n == 1:
        return print(1)
    if n%2 == 1:
        func(3*n+1)
    else:
        func(n//2)
    return print(n)
    
func(n)