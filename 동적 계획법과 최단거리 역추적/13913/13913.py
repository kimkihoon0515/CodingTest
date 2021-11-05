from collections import deque

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            result = [] 
            while x != n: # 결과값에 경로 값을 거슬러 올라가면서 저장
                result.append(x)
                x = li[x]
            result.append(n)
            result.reverse()  # 역순으로 저장되어 있으므로 순서를 바꿈
            print(' '.join(map(str, result)))
            return
        for i in (x-1, x+1, x*2):  # -1 +1 *2 를 차례로 하면서 반복문
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[x] + 1 
                queue.append(i)
                li[i] = x  # 이전 위치 저장

n, k = map(int, input().split())

visited = [0] * 100001
li = [0] * 100001
bfs()