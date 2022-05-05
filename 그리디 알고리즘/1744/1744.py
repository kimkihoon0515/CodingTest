from re import L
import sys

n = int(sys.stdin.readline())

li = sorted([int(sys.stdin.readline()) for _ in range(n)])

minus = []

plus = []

one = [] # 1로만 이루어진 배열

for i in range(len(li)):
    if li[i] <= 0 :
        minus.append(li[i])
    elif li[i]>1:
        plus.append(li[i])
    else:
        one.append(li[i]) 
plus = sorted(plus,reverse=True)

ans = 0
if len(plus) % 2 == 0:
    for i in range(0,len(plus),2):
        ans += plus[i]*plus[i+1]
else:
    for i in range(0,len(plus)-1,2):
        ans += plus[i]*plus[i+1]
    ans += plus[-1]

if len(minus)%2 == 0:
    for i in range(0,len(minus),2):
        ans += minus[i]*minus[i+1]
else:
    for i in range(0,len(minus)-1,2):
        ans += minus[i]*minus[i+1]
    ans += minus[-1]
ans += sum(one) 
print(ans)