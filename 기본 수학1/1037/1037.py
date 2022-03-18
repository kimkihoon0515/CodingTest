import sys

a = int(sys.stdin.readline())

li = sorted(list(map(int,sys.stdin.readline().split())))

if len(li) == 1:
    print(li[0]**2)
else:
    print(li[0]*li[-1])