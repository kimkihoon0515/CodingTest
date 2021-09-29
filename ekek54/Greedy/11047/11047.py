import sys
N, K= map(int,sys.stdin.readline().split(' '))
arr = [int(sys.stdin.readline()) for i in range(N)]
arr.reverse()
sum=0
for i in arr:
    if i <= K:
        sum += K//i
        K = K % i
    if K == 0:
        break
print(sum)