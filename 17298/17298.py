""" 이중 for문을 돌리면 시간복잡도가 O(n^2)이 되므로 시간초과발생
import sys
n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

li = []

for i in range(len(a)):
    cnt = 0
    for j in a[i+1:]:
        if j>a[i]:
            li.append(j)
            break
        if j <= a[i]:
            cnt+=1 
        if cnt == (len(a)-i-1):
            li.append(-1)
    if i == (len(a)-1):
        li.append(-1)
print(*li)
"""
import sys

n = int(sys.stdin.readline()) # 크기가 n인 배열을 입력한다.

a = list(map(int,sys.stdin.readline().split()))
result = [-1] * n # 결과값을 저장하는 배열을 만든다.
li = [] # 인덱스를 넣어 주기 위한 배열

li.append(0)
for i in range(1,n):
    while li and a[li[-1]] < a[i]: 
        result[li.pop()] = a[i]
    li.append(i)

print(*result)