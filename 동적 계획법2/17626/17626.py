from random import randrange
import sys
import math

n = int(sys.stdin.readline().strip())

li = []
ans = 4

for i in range(224):
    li.append(i**2)
    

for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            if li[i]+li[j]+li[k] == n:
                ans = 3

for i in range(len(li)):
    for j in range(len(li)):
        if li[i]+li[j] == n:
            ans = 2

for i in range(len(li)):
    if li[i] == n:
        ans = 1

print(ans)