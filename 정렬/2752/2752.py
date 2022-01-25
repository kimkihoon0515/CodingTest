import sys

li = list(map(int,sys.stdin.readline().split()))

print(*sorted(li))