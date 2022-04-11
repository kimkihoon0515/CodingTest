from collections import deque
import sys

def get_prime_nums():
    prime = [True] * 10000
    prime[0], prime[1] = False, False
    
    for i in range(2, 10000):
        if prime[i] == True:
            j = 2

            while i * j < 10000:
                prime[i * j] = False
                j += 1

    return prime

def bfs(start, target):
    q = deque()
    # 시작점과 카운트
    q.append([start, 0])
    visited = [False] * 10000
    visited[start] = True

    while q:
        current, cnt = q.popleft()

        if current == target:
            return cnt
        
        current = str(current)

        for i in range(4):
            for j in range(10):
                temp = int(current[:i] + str(j) + current[i+1:])

                if not visited[temp] and prime_nums[temp] and temp >= 1000:
                    visited[temp] = True
                    q.append([temp, cnt+1])
    # 불가능
    return None

if __name__ == "__main__":
    n = int(input())
    prime_nums = get_prime_nums()
    ans = []
    for _ in range(n):
        start, target = map(int, input().split())
        ans.append(bfs(start, target))

    for x in ans:
        if x == None:
            print("Impossible")
        
        else:
            print(x)