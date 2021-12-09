import sys
import math

n,k = map(int,sys.stdin.readline().split())

arr = [True for i in range(n+1)]

result = []
cnt = 0
for i in range(2,n+1):
    if arr[i] == True:
        j = 1
        while i * j <=n:
            if arr[i*j] == True:
                arr[i*j] = False
                cnt +=1
                result.append([cnt,i*j])
                j+=1
            else:
                j +=1
for a,b in result:
    if a == k:
        print(b)