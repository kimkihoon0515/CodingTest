import sys

n,m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

answer = sorted(a+b)

print(*answer)