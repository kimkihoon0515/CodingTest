import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline().strip())

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)
print(fac(n))
