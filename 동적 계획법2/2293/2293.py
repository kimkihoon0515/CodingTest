import  sys

n,k = map(int,sys.stdin.readline().split()) # n 종류의 동전을 합쳐서 k 가치가 되도록. 동전의 개수는 무한대
li = [] # [1,2,5]
for _ in range(n): 
    li.append(int(sys.stdin.readline()))
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in li:
    for j in range(1,k+1):
        if j>=i:
            dp[j] +=dp[j-i]

print(dp[k])