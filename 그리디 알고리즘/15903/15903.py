import sys

n,m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    a = sorted(a) # 최소값을 구해야하므로
    new_card = a[0]+a[1] # 문제조건
    a[0] = new_card # 가장 작은 2개의 카드를 새롭게 정의한 카드로 바꿔준다.
    a[1] = new_card
    
print(sum(a))