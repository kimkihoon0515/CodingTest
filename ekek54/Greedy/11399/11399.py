import sys
N= int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split(' ')))
## 기다리는 시간의 최소화는 SJF를 사용
arr.sort()
lis=[]
tmp=0
for i in arr:
    tmp += i
    lis.append(tmp)
print(sum(lis))
