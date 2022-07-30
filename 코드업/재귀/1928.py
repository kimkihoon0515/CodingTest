import sys

n = int(sys.stdin.readline())

def func(n):
    print(n)
    if n == 1:
        return
    elif n%2==0:
        n = n//2
    elif n%2!=0:
        n = 3*n+1
    func(n)

func(n)
