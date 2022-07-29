import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
ans = 0
def dfs(n):
    global ans
    if n == 0:
        return ans
    ans+=n
    dfs(n-1)

dfs(n)
print(ans)
