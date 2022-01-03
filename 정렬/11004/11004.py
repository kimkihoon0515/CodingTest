import sys

n,k = map(int,sys.stdin.readline().split())

li = sorted(list(map(int,sys.stdin.readline().split())))

print(li[k-1])