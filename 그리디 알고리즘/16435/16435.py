import sys

n,l = map(int,sys.stdin.readline().split())

h = list(map(int,sys.stdin.readline().split()))
h.sort()

for i in h:
    if i > l:
        break
    elif i <= l:
        l+=1

print(l)