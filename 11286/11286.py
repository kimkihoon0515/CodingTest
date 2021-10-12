import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(heap)[1]) # 출력시킬때는 입력값을 다시 출력해야 하므로 [|x|,x] 중에서 오른쪽 값을 출력해야한다.
        except:
            print(0)
    else:
        heapq.heappush(heap,(abs(x),x)) # heap에 넣을 때 절대값을 함께 넣어주면 그 절대값을 기준으로 정렬을 한다. 
