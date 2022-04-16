# 어려워서 풀이를 참조했음 

import sys
from collections import deque

def bfs(g):
    q = deque()
    check = [False for _ in range(n)]
    q.append(g[0])
    check[g[0]] = True

    cnt, answer = 1, 0
    while q:
        temp = q.popleft()
        answer += people[temp]
        for i in board[temp]:
            # i는 인접한 값인데
            # 그 값이 g배열안에 있고 방문한적이 없더라면 계속 진행가능
            if i in g and not check[i]:
                check[i] = True
                cnt += 1
                q.append(i)

    if cnt == len(g):
        return answer
    else:
        return False


def dfs(cnt, x, end):
    global min_value

    # 원하는 구역의 개수만큼 도달했을 때
    if cnt == end:
        g1, g2 = deque(), deque()

        # 방문했으면 g1그룹으로 방문하지 않았으면 g2그룹으로 넣어준다
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)

        # bfs를 통해 g1 deque안의 값이 인정한 값인지 확인
        ans1 = bfs(g1)

        # 아니라면 함수 바로 종료
        if not ans1:
            return

        # bfs를 통해 g2 deque안의 값이 인정한 값인지 확인
        ans2 = bfs(g2)

        # 아니라면 함수 바로 종료
        if not ans2:
            return

        # g1, g2둘다 인접한 구인지 확인이 되었다면 최소값 확인
        min_value = min(min_value, abs(ans1-ans2))
        return

    # 아직 end개수에 도달하지 못했을때는
    # for문을 통해 그 다음구역부터 새로운 구를 만들어준다.
    for i in range(x, n):
        # 방문을 했다면 무시
        if visited[i]:
            continue

        # 방문을 안했다면 visited 배열 바꿔주고 dfs탐색 시작
        visited[i] = True
        dfs(cnt+1, i, end)

        # back tracking
        visited[i] = False


n = int(input())
people = list(map(int, input().split()))

board = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        board[i].append(j-1)

min_value = sys.maxsize
# 선거구가 2개로 나누어지기 때문에 n//2까지만 확인하면 된다.
for i in range(1, n//2 + 1):
    visited = [False for _ in range(n)]
    # 구역 찾기
    dfs(0, 0, i)


if min_value == sys.maxsize:
    print(-1)
else:
    print(min_value)