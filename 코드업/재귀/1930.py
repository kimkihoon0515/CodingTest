import sys

sys.setrecursionlimit(1000000)

def supersum(a,b):
    if a == 0:
        return b
    if dp[a][b] == -1:
        summary = 0
        for i in range(1,b+1):
            summary += supersum(a-1,i)
        dp[a][b] = summary
        return summary
    else:
        return dp[a][b]       

while True:
    try:
        a,b = map(int,sys.stdin.readline().split())
        dp = [[-1 for i in range(b+1)] for _ in range(a+1)]
        print(supersum(a,b))
    except:
        break