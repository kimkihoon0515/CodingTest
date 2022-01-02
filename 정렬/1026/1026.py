import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a = sorted(a,reverse=True) # 역순 정렬
b = sorted(b) # 순서 정렬

answer = 0
for i in range(n):
    answer += a[i]*b[i]
print(answer)