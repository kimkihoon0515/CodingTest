# bellman ford로 푸는 문제이다.
# queue에 넣고 최소 가중치를 찾는 것이 아니라 모든 정점에 연결되어 있는 것들을 n-1번 반복
# n-1 때도 update가 된다면 음의 가중치가 있는 것이다.
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)
dp[1] = 0
isPossible = True

def bellmanFord():
    global isPossible
    
    for repeat in range(n): # 시작점에서 각 정점에 걸리는 시간을 저장하는 배열
        for i in range(1, n + 1):
            for n_n, wei in graph[i]:
                if dp[i] != inf and dp[n_n] > dp[i] + wei:
                    dp[n_n] = dp[i] + wei # 간선 1부터 계속 걸리는 시간을 update해준다.
                    if repeat == n - 1:
                        isPossible = False

for _ in range(m):
    a, b, c = map(int ,input().split())
    graph[a].append([b, c])


bellmanFord()

if not isPossible:
    print(-1)
else:
    for i in dp[2:]:
        print(i if i != inf else -1)