'''
import sys
import math

def number(k):
    if k == 1 or k == 2:
        return False
    for i in range(2,int(math.sqrt(k))):
        if k % i == 0:
            return True
    return False

def prime(k):
    ans = [True]*k*2
    for i in range(2,int(math.sqrt(2*k))+1):
        if ans[i] == True:
            for j in range(i+i,2*k,i):
                ans[j] = False
    answer = [i for i in range(2,2*k) if ans[i] == True]
    for i in range(len(answer)):
        if answer[i]> k:
            return answer[i-1],answer[i]
        
t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline().strip())
    if number(k):
        print(prime(k)[-1]-prime(k)[-2])
    else:
        print(0)
'''        
        
import sys
import math

max = 1299709


ans = [True]*max
for i in range(2,int(math.sqrt(max))+1):
    if ans[i]== True:
        for j in range(i+i,max,i):
            ans[j] = False
answer = [i for i in range(2,max) if ans[i]==True]

def prime(k):
    if k in answer:
        return True
    return False

def binsearch(k):
    left = 2
    right = max
    while left <= right:
        mid = (left+right) // 2
        if mid <= k:
            mid = left + 1
        else:
            mid = right - 1
    return left
            
    
t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline().strip())
    if prime(k):
        print(binsearch(k))
    else:
        print(0)