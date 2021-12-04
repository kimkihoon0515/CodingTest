import sys

li = list(map(int,sys.stdin.readline().split()))

li.sort(reverse = True)
print(li[-2])