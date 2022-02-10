import sys

n = int(sys.stdin.readline())

ans = [0,1,3]

for i in range(3,n+1):
    ans.append(ans[i-2]*2 + ans[i-1])

print(ans[n]%10007)
